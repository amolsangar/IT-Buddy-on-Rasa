## restart conversation & set user details
* email.id
  - action_set_user_details_slot
  - slot{"email_id": "amol.sangar@t-systems.com"}
  - slot{"company_name": "T-Systems ICT India Pvt. Ltd."}
  - slot{"first_name": "Amol"}
  - slot{"last_name": "Sangar"}
  - slot{"user_name": "A90431271"}

## say hi with user_name
* say_hi
  - utter_say_hi_user_name

## it issue story
* new_it_issue
  - utter_new_it_issue_template

## other question
* other
  - utter_other_response

## printer issue no path
* printer_issue
  - printer_issue_form
  - form{"name": "printer_issue_form"}
  - form{"name": null}
  - utter_is_problem_solved
* confirmation.no
  - action_create_ticket
  - action_db_operation
  - slot{"email_id": "amol.sangar@t-systems.com"}
  - slot{"company_name": "T-Systems ICT India Pvt. Ltd."}
  - slot{"first_name": "Amol"}
  - slot{"last_name": "Sangar"}
  - slot{"user_name": "A90431271"}

## printer issue yes path
* printer_issue
  - printer_issue_form
  - form{"name": "printer_issue_form"}
  - form{"name": null}
  - utter_is_problem_solved
* confirmation.yes
  - utter_user.excited
  - action_db_operation
  - slot{"email_id": "amol.sangar@t-systems.com"}
  - slot{"company_name": "T-Systems ICT India Pvt. Ltd."}
  - slot{"first_name": "Amol"}
  - slot{"last_name": "Sangar"}
  - slot{"user_name": "A90431271"}

## fmb dl issue no path
* fml_dl_issue
  - fml_dl_issue_form
  - form{"name": "fml_dl_issue_form"}
  - form{"name": null}
  - utter_is_problem_solved
* confirmation.no
  - action_create_ticket
  - action_db_operation
  - slot{"email_id": "amol.sangar@t-systems.com"}
  - slot{"company_name": "T-Systems ICT India Pvt. Ltd."}
  - slot{"first_name": "Amol"}
  - slot{"last_name": "Sangar"}
  - slot{"user_name": "A90431271"}

## fmb dl issue yes path
* fml_dl_issue
  - fml_dl_issue_form
  - form{"name": "fml_dl_issue_form"}
  - form{"name": null}
  - utter_is_problem_solved
* confirmation.yes
  - utter_user.excited
  - action_db_operation
  - slot{"email_id": "amol.sangar@t-systems.com"}
  - slot{"company_name": "T-Systems ICT India Pvt. Ltd."}
  - slot{"first_name": "Amol"}
  - slot{"last_name": "Sangar"}
  - slot{"user_name": "A90431271"}

## bitlocker issue no path
* bitlocker_issue
  - bitlocker_issue_form
  - form{"name": "bitlocker_issue_form"}
  - form{"name": null}
  - utter_is_problem_solved
* confirmation.no
  - action_create_ticket
  - action_db_operation
  - slot{"email_id": "amol.sangar@t-systems.com"}
  - slot{"company_name": "T-Systems ICT India Pvt. Ltd."}
  - slot{"first_name": "Amol"}
  - slot{"last_name": "Sangar"}
  - slot{"user_name": "A90431271"}

## bitlocker issue yes path
* bitlocker_issue
  - bitlocker_issue_form
  - form{"name": "bitlocker_issue_form"}
  - form{"name": null}
  - utter_is_problem_solved
* confirmation.yes
  - utter_user.excited
  - action_db_operation
  - slot{"email_id": "amol.sangar@t-systems.com"}
  - slot{"company_name": "T-Systems ICT India Pvt. Ltd."}
  - slot{"first_name": "Amol"}
  - slot{"last_name": "Sangar"}
  - slot{"user_name": "A90431271"}

## vpn issue no path 
* vpn_issue
  - vpn_issue_form
  - form{"name": "vpn_issue_form"}
  - form{"name": null}
  - utter_is_problem_solved
* confirmation.no
  - action_create_ticket
  - action_db_operation
  - slot{"email_id": "amol.sangar@t-systems.com"}
  - slot{"company_name": "T-Systems ICT India Pvt. Ltd."}
  - slot{"first_name": "Amol"}
  - slot{"last_name": "Sangar"}
  - slot{"user_name": "A90431271"}

## vpn issue yes path
* vpn_issue
  - vpn_issue_form
  - form{"name": "vpn_issue_form"}
  - form{"name": null}
  - utter_is_problem_solved
* confirmation.yes
  - utter_user.excited
  - action_db_operation
  - slot{"email_id": "amol.sangar@t-systems.com"}
  - slot{"company_name": "T-Systems ICT India Pvt. Ltd."}
  - slot{"first_name": "Amol"}
  - slot{"last_name": "Sangar"}
  - slot{"user_name": "A90431271"}

## internet wifi issue no path
* internet_wifi_issue
  - internet_wifi_issue_form
  - form{"name": "internet_wifi_issue_form"}
  - form{"name": null}
  - utter_is_problem_solved
* confirmation.no
  - action_create_ticket
  - action_db_operation
  - slot{"email_id": "amol.sangar@t-systems.com"}
  - slot{"company_name": "T-Systems ICT India Pvt. Ltd."}
  - slot{"first_name": "Amol"}
  - slot{"last_name": "Sangar"}
  - slot{"user_name": "A90431271"}

## internet wifi issue yes path 
* internet_wifi_issue
  - internet_wifi_issue_form
  - form{"name": "internet_wifi_issue_form"}
  - form{"name": null}
  - utter_is_problem_solved
* confirmation.yes
  - utter_user.excited
  - action_db_operation
  - slot{"email_id": "amol.sangar@t-systems.com"}
  - slot{"company_name": "T-Systems ICT India Pvt. Ltd."}
  - slot{"first_name": "Amol"}
  - slot{"last_name": "Sangar"}
  - slot{"user_name": "A90431271"}


## jabber issue no path
* jabber_issue
  - jabber_issue_form
  - form{"name": "jabber_issue_form"}
  - form{"name": null}
  - utter_is_problem_solved
* confirmation.no
  - action_create_ticket
  - action_db_operation
  - slot{"email_id": "amol.sangar@t-systems.com"}
  - slot{"company_name": "T-Systems ICT India Pvt. Ltd."}
  - slot{"first_name": "Amol"}
  - slot{"last_name": "Sangar"}
  - slot{"user_name": "A90431271"}

## jabber issue yes path 
* jabber_issue
  - jabber_issue_form
  - form{"name": "jabber_issue_form"}
  - form{"name": null}
  - utter_is_problem_solved
* confirmation.yes
  - utter_user.excited
  - action_db_operation
  - slot{"email_id": "amol.sangar@t-systems.com"}
  - slot{"company_name": "T-Systems ICT India Pvt. Ltd."}
  - slot{"first_name": "Amol"}
  - slot{"last_name": "Sangar"}
  - slot{"user_name": "A90431271"}

## outlook email issue no path
* outlook_email_issue
  - outlook_email_issue_form
  - form{"name": "outlook_email_issue_form"}
  - form{"name": null}
  - utter_is_problem_solved
* confirmation.no
  - action_create_ticket
  - action_db_operation
  - slot{"email_id": "amol.sangar@t-systems.com"}
  - slot{"company_name": "T-Systems ICT India Pvt. Ltd."}
  - slot{"first_name": "Amol"}
  - slot{"last_name": "Sangar"}
  - slot{"user_name": "A90431271"}

## outlook email issue yes path 
* outlook_email_issue
  - outlook_email_issue_form
  - form{"name": "outlook_email_issue_form"}
  - form{"name": null}
  - utter_is_problem_solved
* confirmation.yes
  - utter_user.excited
  - action_db_operation
  - slot{"email_id": "amol.sangar@t-systems.com"}
  - slot{"company_name": "T-Systems ICT India Pvt. Ltd."}
  - slot{"first_name": "Amol"}
  - slot{"last_name": "Sangar"}
  - slot{"user_name": "A90431271"}

## tiks card issue no path
* tiks_card_issue
  - tiks_card_issue_form
  - form{"name": "tiks_card_issue_form"}
  - form{"name": null}
  - utter_is_problem_solved
* confirmation.no
  - action_create_ticket
  - action_db_operation
  - slot{"email_id": "amol.sangar@t-systems.com"}
  - slot{"company_name": "T-Systems ICT India Pvt. Ltd."}
  - slot{"first_name": "Amol"}
  - slot{"last_name": "Sangar"}
  - slot{"user_name": "A90431271"}

## tiks card issue yes path 
* tiks_card_issue
  - tiks_card_issue_form
  - form{"name": "tiks_card_issue_form"}
  - form{"name": null}
  - utter_is_problem_solved
* confirmation.yes
  - utter_user.excited
  - action_db_operation
  - slot{"email_id": "amol.sangar@t-systems.com"}
  - slot{"company_name": "T-Systems ICT India Pvt. Ltd."}
  - slot{"first_name": "Amol"}
  - slot{"last_name": "Sangar"}
  - slot{"user_name": "A90431271"}

## new it service story
* new_it_service_request
  - new_it_service_request_form
  - form{"name": "new_it_service_request_form"}
  - form{"name": null}
  - action_create_ticket
  - action_db_operation
  - slot{"email_id": "amol.sangar@t-systems.com"}
  - slot{"company_name": "T-Systems ICT India Pvt. Ltd."}
  - slot{"first_name": "Amol"}
  - slot{"last_name": "Sangar"}
  - slot{"user_name": "A90431271"}

## show ticket details
* ticket_details
  - ticket_details_form
  - form{"name": "ticket_details_form"}
  - form{"name": null}


## say goodbye
* greetings.bye
  - utter_greetings.bye

## greeting
* greetings.hello
  - utter_greetings.hello
  - utter_default_template

## thanks
* thanks
    - utter_appraisal.well_done

## abuse
* abuse
	- utter_abuse_response

## password reset happy path 1
* password_account_issue
  - password_account_issue_form
  - form{"name": "password_account_issue_form"}
  - form{"name": null}
  - utter_is_problem_solved
* confirmation.no
  - action_create_ticket
  - action_db_operation
  - slot{"email_id": "amol.sangar@t-systems.com"}
  - slot{"company_name": "T-Systems ICT India Pvt. Ltd."}
  - slot{"first_name": "Amol"}
  - slot{"last_name": "Sangar"}
  - slot{"user_name": "A90431271"}

## password reset happy path 2
* password_account_issue
  - password_account_issue_form
  - form{"name": "password_account_issue_form"}
  - form{"name": null}
  - utter_is_problem_solved
* confirmation.yes
  - utter_user.excited
  - action_db_operation
  - slot{"email_id": "amol.sangar@t-systems.com"}
  - slot{"company_name": "T-Systems ICT India Pvt. Ltd."}
  - slot{"first_name": "Amol"}
  - slot{"last_name": "Sangar"}
  - slot{"user_name": "A90431271"}

## stop but continue path 1
* password_account_issue
    - password_account_issue_form
    - form{"name": "password_account_issue_form"}
* stop
    - utter_ask_continue
* confirmation.yes
    - password_account_issue_form
    - form{"name": null}
 	- utter_is_problem_solved
* confirmation.yes
    - utter_user.excited

## stop but continue path 2
* password_account_issue
    - password_account_issue_form
    - form{"name": "password_account_issue_form"}
* stop
    - utter_ask_continue
* confirmation.yes
    - password_account_issue_form
    - form{"name": null}
    - utter_is_problem_solved
* confirmation.no
    - utter_raise_ticket

## stop and really stop path
* password_account_issue
    - password_account_issue_form
    - form{"name": "password_account_issue_form"}
* stop
    - utter_ask_continue
* confirmation.no
    - action_deactivate_form
    - form{"name": null}

## Generated Story 4001381340481127785
* password_account_issue
    - password_account_issue_form
    - form{"name": "password_account_issue_form"}
    - slot{"requested_slot": "account_type"}
* stop
    - utter_ask_continue
* confirmation.no
    - action_deactivate_form
    - form{"name": null}
    - slot{"requested_slot": null}
* greetings.bye
    - utter_greetings.bye

## Generated Story 6983885463072510061
* say_hi
    - utter_say_hi_user_name
