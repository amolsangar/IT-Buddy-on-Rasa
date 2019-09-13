from typing import Dict, Text, Any, List, Union, Optional

from rasa_sdk import Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.forms import FormAction
from rasa_sdk.events import SlotSet 


class VPNIssueForm(FormAction):
    """Example of a custom form action"""

    def name(self) -> Text:
        """Unique identifier of the form"""
        
        return "vpn_issue_form"

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
            intent = 'vpn_issue'

        loc_name = tracker.get_slot('loc_name');
        if "pune" in loc_name.lower():
            problemID = 58
        elif "blr" in loc_name.lower():
            problemID = 108
        else:
            problemID = 58
        
        link = ""
        guide = '<a href="file://10.197.192.69/Common/IT/Helpdesk%20Doc/ChatBot/Global%20Remote%20Connectivity%20Guide.docx" target="_blank"><b>Remote Access VPN Support Guide</b></a>'
        response = "Please check that you have a good internet connection. While using hotspot please use 3G as preferred network. If you are traveling and in hotel, please note some hotels block VPN access from their wireless network. <br>Here is a step wise guide to help you solve Global Remote/VPN connectivity issues. <br><br>{}".format(guide)
        dispatcher.utter_message(response)

        return [SlotSet("subject",subject),
        SlotSet("prob_type", problemID),
        SlotSet("intent_name", intent)]