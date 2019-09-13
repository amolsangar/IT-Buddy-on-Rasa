from rasa_sdk import Action
from rasa_sdk.events import SlotSet
from typing import Dict, Text, Any, List, Union, Optional
from rasa_sdk import Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import Restarted
import json
import requests
import pyodbc 
import time
import asyncio

async def get_user_tracker(user_name):
  url = "http://localhost:5005/conversations/{}/tracker".format(user_name)
  resp = requests.get(url)

  if resp.status_code != 200:
    print('Error: Rest API Error with Status Code: ' + str(resp.status_code))
    return None
  else:
    obj = json.loads(resp.content)
    #for key in obj[0]:
      #print(obj[0][key])
    #print(obj[0]['id'])
    return obj

async def store_in_db(myDict):
  user_name = myDict['user_name']
  first_name = myDict['first_name']
  last_name = myDict['last_name']
  email = myDict['email']
  generated_ticket_number = myDict['generated_ticket_number']
  solved = myDict['solved']
  intent = myDict['intent']

  obj = await asyncio.ensure_future(get_user_tracker(user_name))  # fire and forget async_foo()

  if(obj):
    print("Commencing conversation insert into DB")
    conv_str = json.dumps(obj)
    conv_str = conv_str.replace("'", "''")
    conversation_details = conv_str;
    if not generated_ticket_number:
      generated_ticket_number = ''
    if not solved:
      solved = 'YES'
    
    solved = solved.upper()

  conn = pyodbc.connect('Driver={SQL Server};'
                        'Server=10.197.194.145;'
                        'Database=T-BOT;'
                        'uid=sa;'
                        'pwd=Pass-w0rd;'
                        )

  cursor = conn.cursor()

  sql_insert_query_1 = "EXEC [T-BOT].[dbo].[conv_insert] @a_id='{}',@first_name='{}',@last_name='{}',@email='{}',@conv_details='{}',@ticket_no='{}',@intent='{}',@is_solved='{}'".format(user_name, first_name, last_name, email, conversation_details, generated_ticket_number, intent, solved)
  #print(sql_insert_query_1)
  cursor.execute(sql_insert_query_1)
  conn.commit()
  
  cursor.close()

class ActionDBOperation(Action):
   def name(self) -> Text:
      return "action_db_operation"

   def run(self,
           dispatcher: CollectingDispatcher,
           tracker: Tracker,
           domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

      print("Custom Action - DB Operation Invoked!!");

      
      email = str(tracker.get_slot('email_id'))
      client_id = tracker.get_slot('client_id');
      company_name = tracker.get_slot('company_name');
      dept_id = tracker.get_slot('dept_id');
      dept_name = tracker.get_slot('dept_name');
      loc_id = tracker.get_slot('loc_id');
      loc_name = tracker.get_slot('loc_name');
      first_name = str(tracker.get_slot('first_name'))
      last_name = str(tracker.get_slot('last_name'))
      
      user_name = str(tracker.get_slot('user_name'))

      generated_ticket_number = tracker.get_slot('generated_ticket_number')
      solved = tracker.get_slot('solved')
      intent = tracker.get_slot('intent_name');
      #intent = str(tracker.latest_message['intent'].get('name'))

      # waiting so that the tracker is updated by that time
      time.sleep(1)

      myDict = {
        "user_name": user_name,
        "first_name": first_name,
        "last_name": last_name,
        "email": email,
        "generated_ticket_number": generated_ticket_number,
        "solved": solved,
        "intent": intent
      }

      loop = asyncio.get_event_loop()
      loop.run_until_complete(store_in_db(myDict))
      
      return [Restarted(),
      SlotSet("email_id", email),
      SlotSet("client_id", client_id),
      SlotSet("company_name", company_name),
      SlotSet("dept_id", dept_id),
      SlotSet("dept_name", dept_name),
      SlotSet("loc_id", loc_id),
      SlotSet("loc_name", loc_name),
      SlotSet("first_name", first_name),
      SlotSet("last_name", last_name),
      SlotSet("user_name", user_name)
      ]

   
