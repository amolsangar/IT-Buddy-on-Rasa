from typing import Dict, Text, Any, List, Union, Optional

from rasa_sdk import Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.forms import FormAction
from rasa_sdk.events import SlotSet 


class PasswordAccountIssueForm(FormAction):
    """Example of a custom form action"""

    def name(self) -> Text:
        """Unique identifier of the form"""
        
        return "password_account_issue_form"

    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:
        """A list of required slots that the form has to fill"""

        return ["account_type"]

    def slot_mappings(self) -> Dict[Text, Union[Dict, List[Dict]]]:
        """A dictionary to map required slots to
            - an extracted entity
            - intent: value pairs
            - a whole message
            or a list of them, where a first match will be picked"""

        return {
            "account_type": self.from_entity(entity="account_type", intent=["inform","password_account_issue"]),
        }

    # USED FOR DOCS: do not rename without updating in docs
    def account_type_db(self) -> List[Text]:
        """Database of supported cuisines"""

        return [
            "wiw",
            "emea2",
            "windows",
            "ciam"
        ]

    # USED FOR DOCS: do not rename without updating in docs
    def validate_account_type(
        self,
        value: Text,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> Optional[Text]:
        """Validate cuisine value."""

        if value.lower() in self.account_type_db():

            # validation succeeded, set the value of the "cuisine" slot to value
            return {"account_type": value}
        else:
            dispatcher.utter_template("utter_wrong_account_type", tracker)
            # validation failed, set this slot to None, meaning the
            # user will be asked for the slot again
            return {"account_type": None}

    def submit(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict]:
        """Define what the form has to do
            after all required slots are filled"""

        acc_type = tracker.get_slot('account_type');
        if(tracker.active_form.get('trigger_message')):
            subject = tracker.active_form.get('trigger_message')['text'] + str(" : ") + str(acc_type);
            intent = str(tracker.active_form.get('trigger_message')['intent']['name'])
        else:
            subject = tracker.latest_message.get('text');
            intent = 'password_account_issue'

        if(acc_type.lower() == 'emea2' or acc_type.lower() == 'windows'):

            problemID = 68
            link = "<a href='https://myit.telekom.de/PM' target='_blank'>Password Management</a>"
            guide = '<a href="file://10.197.192.69/Common/IT/Helpdesk%20Doc/ChatBot/Windows%20or%20EMEA2%20Account.pdf" target="_blank"><b>EMEA2 Support Guide</b></a>'
            response = "To reset or unlock your EMEA2 account password from any PC, please ensure you complete your profile at {} Tool (with PIN set, security questions etc.). <br>Refer attached guide for the same. <br><br>{}".format(link,guide)
            dispatcher.utter_message(response)

        if(acc_type.lower() == 'wiw'):

            problemID = 67
            link = "<a href='https://websso.t-systems.com/wiw/wiwauth/uss' target='_blank'><b>WIW</b></a>"
            guide = '<a href="file://10.197.192.69/Common/IT/Helpdesk%20Doc/ChatBot/WIW%20&%20Windows%20Password%20Reset%20Procedure.pdf" target="_blank"><b>WIW Support Guide</b></a>'
            response = "To change or reset your WiW password, please follow below steps - <br>1. Go to {} <br>2. On home page, select appropriate option and enter your details <br>3. You will get an option to change WIW password with the help of security question/answer. <br>4. If there is any problem with your account or you do not remember the security question/answer to reset password, please call the WIW Service Desk on +49 391 5976 2317. <br>For more information and WiW registration, please refer attached guide <br><br>{}".format(link,guide)
            dispatcher.utter_message(response)

        if(acc_type.lower() == 'ciam' or acc_type.lower() == 'jabber'):

            problemID = 70
            link = "<a href='mailto:Myportal.Support@telekom.de?Subject='><b>FMB Myportal Support</b></a>"
            guide = '<a href="file://10.197.192.69/Common/IT/Helpdesk%20Doc/ChatBot/CIAM%20Registration%20&%20Jabber%20Account%20requisition%20Procedure%20for%20New%20Users.pdf" target="_blank"><b>CIAM Registration & Jabber Account Requisition Procedure Guide</b></a>'
            response = "If your CIAM account is locked, please send an email to - {} with the error screenshot. <br>To reset your CIAM or Jabber password, please refer below guide. <br><br>{}".format(link,guide)
            dispatcher.utter_message(response)


        return [SlotSet("account_type", None),
        SlotSet("subject",subject),
        SlotSet("prob_type", problemID),
        SlotSet("intent_name", intent)]