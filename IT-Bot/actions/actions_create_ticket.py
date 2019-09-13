from rasa_sdk import Action
from rasa_sdk.events import SlotSet
from typing import Dict, Text, Any, List, Union, Optional
from rasa_sdk import Tracker
from rasa_sdk.executor import CollectingDispatcher
import json
import requests

class ActionCreateTicket(Action):
   def name(self) -> Text:
      return "action_create_ticket"

   def run(self,
           dispatcher: CollectingDispatcher,
           tracker: Tracker,
           domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

      print("Custom Action - Create Ticket Invoked!!");

      email = tracker.get_slot('email_id');
      client_id = tracker.get_slot('client_id');
      company_name = tracker.get_slot('company_name');
      dept_id = tracker.get_slot('dept_id');
      dept_name = tracker.get_slot('dept_name');
      loc_id = tracker.get_slot('loc_id');
      loc_name = tracker.get_slot('loc_name');
      first_name = tracker.get_slot('first_name');
      last_name = tracker.get_slot('last_name');
      user_name = tracker.get_slot('user_name');
      prob_type = tracker.get_slot('prob_type');
      intent_name = tracker.get_slot('intent_name');

      subject = tracker.get_slot('subject');
      if not subject:
        return []

      subject = subject.replace('_',' ');
      subject = subject.replace('/','');

      url = "http://supportcenter.in.t-internal.com/helpdesk/WebObjects/Helpdesk.woa/ra/Tickets?apiKey=VTEXGXaHe0fvMK1wS0kie7U1e4umXMNv5UM1a1UK";
      data = {
          "room": "",
          "emailClient": True,
          "emailTech": True,
          "emailTechGroupLevel": False,
          "emailGroupManager": False,
          "emailCc": False,
          "ccAddressesForTech": "",
          "emailBcc": False,
          "bccAddresses": "",
          "subject": subject,
          "detail": "*** Ticket raised from IT Buddy ***",
          "assignToCreatingTech": False,
          "problemtype": {
            "type": "ProblemType",
            "id": prob_type
          },
          "sendEmail": False,
          "location": {
            "type": "Location",
            "id": loc_id
          },
          "department": {
            "type": "Department",
            "id": dept_id
          },
          "clientReporter": {
            "type": "Client",
            "id": client_id
          }
        };

      headers = {"Content-Type": "application/json"}

      resp = requests.post(url, data = json.dumps(data), headers = headers)
      if resp.status_code != 201:
        print('Error: Rest API Error with Status Code: ' + str(resp.status_code))
      else:
        obj = json.loads(resp.content)
        #print(obj)

      if(obj):
        if(intent_name == "new_it_service_request"):
          dispatcher.utter_message("Okay, I have raised an IT Service Request " + str(obj['id']) + " and sent you an email.  Please seek Manager’s approval for your requests and attach it to the ticket " + str(obj['id']) + " for further processing by IT. Meanwhile, I will ask an IT Support Engineer to look into this.");
        else:
          dispatcher.utter_message("I'll ask a support technician to look at it. Meanwhile, I have raised an IT Ticket " + str(obj['id']) + " and sent you an email.");

      return [SlotSet('generated_ticket_number', obj['id']),
      SlotSet("solved", "No"),
      SlotSet("subject", None)]