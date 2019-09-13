from typing import Dict, Text, Any, List, Union, Optional

from rasa_sdk import Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.forms import FormAction
from rasa_sdk.events import SlotSet 


class NewITServiceRequestForm(FormAction):
    """Example of a custom form action"""

    def name(self) -> Text:
        """Unique identifier of the form"""
        
        return "new_it_service_request_form"

    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:
        """A list of required slots that the form has to fill"""

        return ["service_request_type","request_location"]

    def slot_mappings(self) -> Dict[Text, Union[Dict, List[Dict]]]:
        """A dictionary to map required slots to
            - an extracted entity
            - intent: value pairs
            - a whole message
            or a list of them, where a first match will be picked"""

        return {
            "service_request_type": self.from_entity(entity="service_request_type", intent=["get_request_type","new_it_service_request"]),
            "request_location": self.from_entity(entity="request_location", intent=["get_request_location","new_it_service_request"])
        }

    def service_request_type_db(self) -> List[Text]:
        """Database of supported cuisines"""

        return [
            "admin rights",
            "tiks card",
            "url whitelisting",
            "homeshare",
            "commonshare",
            "homeshare or commonshare",
            "tiks",
            "whitelisting",
            "whitelist"
        ]

    def request_location_db(self) -> List[Text]:
        """Database of supported cuisines"""

        return [
            "pune",
            "bangalore"
        ]

    def validate_service_request_type(
        self,
        value: Text,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> Optional[Text]:
        """Validate cuisine value."""

        if value.lower().replace("_"," ") in self.service_request_type_db():

            # validation succeeded, set the value of the "cuisine" slot to value
            return {"service_request_type": value.lower().replace("_"," ")}
        else:
            dispatcher.utter_message("I cannot request this service. I can only request from the options provided")
            # validation failed, set this slot to None, meaning the
            # user will be asked for the slot again
            return {"service_request_type": None}

    def validate_request_location(
        self,
        value: Text,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> Optional[Text]:
        """Validate cuisine value."""

        if value.lower() in self.request_location_db():

            # validation succeeded, set the value of the "cuisine" slot to value
            return {"request_location": value.lower()}
        else:
            dispatcher.utter_message("I cannot request the service at this location. Please select either Pune or Bangalore")
            # validation failed, set this slot to None, meaning the
            # user will be asked for the slot again
            return {"request_location": None}

    def submit(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict]:
        """Define what the form has to do
            after all required slots are filled"""

        req_type = tracker.get_slot('service_request_type');
        req_loc = tracker.get_slot('request_location');

        if(tracker.active_form.get('trigger_message')):
            subject = tracker.active_form.get('trigger_message')['text'] + str(" : ") + str(req_type) + str(" at ") + str(req_loc);
            intent = str(tracker.active_form.get('trigger_message')['intent']['name'])
        else:
            subject = tracker.latest_message.get('text');
            intent = 'new_it_service_request'

        if(req_type.lower() == "admin rights"):

            if(req_loc == "pune"):
                problemID = 85
            elif(req_loc == "bangalore"):
                problemID = 92

        if(req_type.lower() == "tiks card" or req_type.lower() == "tiks"):

            if(req_loc == "pune"):
                problemID = 16
            elif(req_loc == "bangalore"):
                problemID = 101

        if(req_type.lower() == "url whitelisting" or req_type.lower() == "whitelisting" or req_type.lower() == "whitelist"):

            if(req_loc == "pune"):
                problemID = 90
            elif(req_loc == "bangalore"):
                problemID = 102

        if(req_type.lower() == "homeshare or commonshare" or req_type.lower() == "homeshare" or req_type.lower() == "commonshare"):

            if(req_loc == "pune"):
                problemID = 147
            elif(req_loc == "bangalore"):
                problemID = 148

        return [SlotSet("subject",subject),
        SlotSet("prob_type", problemID),
        SlotSet("intent_name", intent)]