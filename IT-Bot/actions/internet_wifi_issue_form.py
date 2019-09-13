from typing import Dict, Text, Any, List, Union, Optional

from rasa_sdk import Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.forms import FormAction
from rasa_sdk.events import SlotSet 


class InternetWIFIIssueForm(FormAction):
    """Example of a custom form action"""

    def name(self) -> Text:
        """Unique identifier of the form"""
        
        return "internet_wifi_issue_form"

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

        user_name = tracker.get_slot('user_name');
        if(tracker.active_form.get('trigger_message')):
            subject = tracker.active_form.get('trigger_message')['text'];
            intent = str(tracker.active_form.get('trigger_message')['intent']['name'])
        else:
            subject = tracker.latest_message.get('text');
            intent = 'internet_wifi_issue'

        loc_name = tracker.get_slot('loc_name');
        if "pune" in loc_name.lower():
            problemID = 61
        elif "blr" in loc_name.lower():
            problemID = 105
        else:
            problemID = 61

        link = ""
        guide = ''
        response = '<div style="word-break: break-all; word-wrap: break-word;">Please follow the below steps to resolve wireless connection issues: <br><br>1. Go to wireless icon & open network and sharing center. <br>If Network connection status continuously blinking, then close that window from task manager and follow below process. <br><br>2. Delete the following file: <br><span style="color:blue">C:/Users/{}/AppData/Roaming/Microsoft/Network/Connections/Pbk/_hiddenPbk/rasphone.pbk</span> <br><br>3. Also check the Wireless Service: <br>i)  Go to Start and open services or press Windows+R and type “servicesmsc” <br>ii) Search for WLAN “AutoConfig” service. Right click and stop start the service.</div>'.format(user_name)
        dispatcher.utter_message(response)

        return [SlotSet("subject",subject),
        SlotSet("prob_type", problemID),
        SlotSet("intent_name", intent)]