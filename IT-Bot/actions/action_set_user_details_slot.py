from rasa_sdk import Action
from rasa_sdk.events import SlotSet
from typing import Dict, Text, Any, List, Union, Optional
from rasa_sdk import Tracker
from rasa_sdk.executor import CollectingDispatcher
import json
import requests

class ActionSetSlot(Action):
   def name(self) -> Text:
      return "action_set_user_details_slot"

   def run(self,
           dispatcher: CollectingDispatcher,
           tracker: Tracker,
           domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

      print("Custom Action Invoked!!");
      #email = tracker.get_slot('email');
      #email = 'amol.sangar@t-systems.com';

      lastest_email_value = next(tracker.get_latest_entity_values("email"), None)

      if((tracker.get_slot('email_id') != lastest_email_value) and tracker.get_slot('email_id')):
        return []

      url = "http://supportcenter.in.t-internal.com/helpdesk/WebObjects/Helpdesk.woa/ra/Clients?qualifier=(email like '" + lastest_email_value + "')&apiKey=VTEXGXaHe0fvMK1wS0kie7U1e4umXMNv5UM1a1UK"
      resp = requests.get(url)

      if resp.status_code != 200:
        print('Error: Rest API Error with Status Code: ' + str(resp.status_code))
      else:
        obj = json.loads(resp.content)
        #for key in obj[0]:
          #print(obj[0][key])
        #print(obj[0]['id'])

      #message = tracker.latest_message.get('text');
      #obj = json.loads(message)
      email = client_id = company_name = dept_id = dept_name = loc_id = loc_name = first_name = last_name = user_name = None;
      if(obj):
        print("CURRENT USER AID : " + obj[0]['username']);
        email_id = obj[0]['email']
        client_id = obj[0]['id']
        company_name = obj[0]['companyName']
        dept_id = obj[0]['department']['id']
        dept_name = obj[0]['department']['name']
        loc_id = obj[0]['location']['id']
        loc_name = obj[0]['location']['locationName']
        first_name = obj[0]['firstName']
        last_name = obj[0]['lastName']
        user_name = obj[0]['username']

      url2 = "http://localhost:5005/conversations/" + user_name + "/tracker/events";
      data2 = [
      {
        "event": "restart"
      },
      {
        "event": "slot",
        "name": "email_id",
        "value": email_id
      },
      {
        "event": "slot",
        "name": "client_id",
        "value": client_id
      },
      {
        "event": "slot",
        "name": "company_name",
        "value": company_name
      },
      {
        "event": "slot",
        "name": "dept_id",
        "value": dept_id
      },
      {
        "event": "slot",
        "name": "dept_name",
        "value": dept_name
      },
      {
        "event": "slot",
        "name": "loc_id",
        "value": loc_id
      },
      {
        "event": "slot",
        "name": "loc_name",
        "value": loc_name
      },
      {
        "event": "slot",
        "name": "first_name",
        "value": first_name
      },
      {
        "event": "slot",
        "name": "last_name",
        "value": last_name
      },
      {
        "event": "slot",
        "name": "user_name",
        "value": user_name
      }
      ];
      headers = {"Content-Type": "application/json"}

      resp2 = requests.post(url2, data = json.dumps(data2), headers= headers)
      if resp2.status_code != 200:
        print('Error: Rest API Error with Status Code: ' + str(resp2.status_code))
      else:
        obj2 = json.loads(resp2.content)
        dispatcher.utter_message(user_name)

      return []

      """return [SlotSet("email_id", email_id),
      SlotSet("client_id", client_id),
      SlotSet("company_name", company_name),
      SlotSet("dept_id", dept_id),
      SlotSet("dept_name", dept_name),
      SlotSet("loc_id", loc_id),
      SlotSet("loc_name", loc_name),
      SlotSet("first_name", first_name),
      SlotSet("last_name", last_name),
      SlotSet("user_name", user_name)
      ]"""