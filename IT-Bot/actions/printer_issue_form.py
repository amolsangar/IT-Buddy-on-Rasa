from typing import Dict, Text, Any, List, Union, Optional

from rasa_sdk import Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.forms import FormAction
from rasa_sdk.events import SlotSet 


class PrinterIssueForm(FormAction):
    """Example of a custom form action"""

    def name(self) -> Text:
        """Unique identifier of the form"""
        
        return "printer_issue_form"

    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:
        """A list of required slots that the form has to fill"""

        return []

    def slot_mappings(self) -> Dict[Text, Union[Dict, List[Dict]]]:
        """A dictionary to map required slots to
            - an extracted entity
            - intent: value pairs
            - a whole message
            or a list of them, where a first match will be picked"""

        return {
        }

    def submit(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict]:
        """Define what the form has to do
            after all required slots are filled"""

        if(tracker.active_form.get('trigger_message')):
            subject = tracker.active_form.get('trigger_message')['text'];
            intent = str(tracker.active_form.get('trigger_message')['intent']['name'])
        else:
            subject = tracker.latest_message.get('text');
            intent = 'printer_issue'

        loc_name = tracker.get_slot('loc_name');
        if "pune" in loc_name.lower():
            problemID = 120
        elif "blr" in loc_name.lower():
            problemID = 119
        else:
            problemID = 120

        link = ""
        guide = '<a href="file://10.197.192.69/Common/IT/Helpdesk%20Doc/ChatBot/Printer%20Support.docx" target="_blank"><b>Printer Support Guide</b></a>'
        response = 'Please follow below steps to get the Printer Access: <br>1.  Press “Windows+R” on your Keyboard. <br>2.  Type, “\\\\10.197.192.69” in Run Command prompt & press Ok <br>3.  Double click/Select a particular floor of which the printer access you need. <br>4.  A Prompt will pop up, select Printer>Printing Preferences>Details>Set a pin>ok <br><br>Please refer below document which will help you with Printer Access. <br>{}'.format(guide)
        dispatcher.utter_message(response)

        return [SlotSet("subject",subject),
        SlotSet("prob_type", problemID),
        SlotSet("intent_name", intent)]