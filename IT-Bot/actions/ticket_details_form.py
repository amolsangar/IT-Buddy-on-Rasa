from typing import Dict, Text, Any, List, Union, Optional
from rasa_sdk import Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.forms import FormAction
from rasa_sdk.events import SlotSet 
import requests
import json
import time

class TicketDetailsForm(FormAction):
    """Example of a custom form action"""

    def name(self) -> Text:
        """Unique identifier of the form"""
        
        return "ticket_details_form"

    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:
        """A list of required slots that the form has to fill"""

        return ["ticket_number"]

    def slot_mappings(self) -> Dict[Text, Union[Dict, List[Dict]]]:

        return {
            "ticket_number": self.from_entity(entity="ticket_number", intent=["inform_ticket_number","ticket_details"]),
        }

    # USED FOR DOCS: do not rename without updating in docs
    def validate_ticket_number(
        self,
        value: Text,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> Optional[Text]:
        """Validate value"""

        if value.isnumeric():
            return {"ticket_number": value}
        else:
            dispatcher.utter_message("Please enter a valid ticket number")
            return {"ticket_number": None}
    
    def submit(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict]:
        """Define what the form has to do
            after all required slots are filled"""

        #my_entity = next(tracker.get_latest_entity_values("ticket_number"), None)
        ticket_no = tracker.get_slot('ticket_number')
        client_id = tracker.get_slot('client_id')

        url = "http://supportcenter.in.t-internal.com/helpdesk/WebObjects/Helpdesk.woa/ra/Tickets?qualifier=((clientId %3D " + str(client_id) + "))&apiKey=VTEXGXaHe0fvMK1wS0kie7U1e4umXMNv5UM1a1UK"
        resp = requests.get(url)
        #time.sleep(1)
        if resp.status_code != 200:
            print('Error: Rest API Error with Status Code: ' + str(resp.status_code))
        else:
            obj = json.loads(resp.content)

        ticket_present = False;
        for x in obj:
            if(str(x['id']) == ticket_no):
                ticket_present = True
                break

        if ticket_present == False:
            temp = obj[0]['id']
            dispatcher.utter_message("Wrong ticket number. Showing your latest ticket.")
        else:
            temp = ticket_no
        
        url2 = "http://supportcenter.in.t-internal.com/helpdesk/WebObjects/Helpdesk.woa/ra/Tickets/" + str(temp) + "?apiKey=VTEXGXaHe0fvMK1wS0kie7U1e4umXMNv5UM1a1UK"
        resp2 = requests.get(url2)
        if resp2.status_code != 200:
            print('Error: Rest API Error with Status Code: ' + str(resp2.status_code))
        else:
            obj2 = json.loads(resp2.content)


        if(obj2):
            tid = obj2['id']
            sub = obj2['subject']
            reportDate = obj2['reportDateUtc'][:10];
            if(obj2['clientTech']):
                client_tech = obj2['clientTech']['displayName']
                email = "<a href='mailto:{}?Subject=Ticket%20Number%20{}'>{}</a>".format(obj2['clientTech']['email'], tid, client_tech)
            else:
                email = 'Not yet assigned'

            status = obj2['statustype']['statusTypeName'] 
            if(obj2['notes']):
                note = obj2['notes'][0]['mobileNoteText']
            else:
                note = 'Empty'
            #add_note = "<a href='mailto:FMB.FMB-TSIN-IT-Support-Center@t-systems.com?subject=Ticket%3a{}%20Action%3aUpdate&body=REPLACE%20THIS%20TEXT%20WITH%20YOUR%20NOTE%20FOR%20TICKET%205038.%20Do%20not%20include%20your%20signature.%20'>Add Note</a>".format(tid)
            #cancel_ticket = "<a href='mailto:FMB.FMB-TSIN-IT-Support-Center@t-systems.com?subject=Ticket%3a{}%20Action%3aCancel&body=Send%20this%20message%20to%20cancel%20Ticket%205038.%20The%20message%20body%20will%20be%20ignored.'>Cancel Ticket</a>".format(tid)
            #more_details = "<a href='http://supportcenter.in.t-internal.com/helpdesk/WebObjects/Helpdesk.woa/wo/.9.1.3'>More Details</a>"
            message = "<b>Ticket Details:</b><br><b>No</b>: {} <br><b>Report Date</b>: {} <br><b>Subject</b>: {} <br><b>Ticket Assigned to</b>: <br>{} <br><b>Status</b>: {} <br><b>Latest Note</b>: {} <br>".format(tid,reportDate,sub,email,status,note)

        dispatcher.utter_message(message)

        return [SlotSet("ticket_number",None)]