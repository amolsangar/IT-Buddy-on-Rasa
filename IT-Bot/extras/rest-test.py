import requests
import json

#url = "http://supportcenter.in.t-internal.com/helpdesk/WebObjects/Helpdesk.woa/ra/Clients/A90431272?apiKey=VTEXGXaHe0fvMK1wS0kie7U1e4umXMNv5UM1a1UK";
"""email = 'amol.sangar@t-systems.com';
url = "http://supportcenter.in.t-internal.com/helpdesk/WebObjects/Helpdesk.woa/ra/Clients?qualifier=(email like '" + email + "')&apiKey=VTEXGXaHe0fvMK1wS0kie7U1e4umXMNv5UM1a1UK";
resp = requests.get(url)
if resp.status_code != 200:
    print('Error: Rest API Error')
else:
	obj = json.loads(resp.content)
	for key in obj[0]:
		print(obj[0][key]);
	#print(obj)"""

url = "http://supportcenter.in.t-internal.com/helpdesk/WebObjects/Helpdesk.woa/ra/Clients?qualifier=(email like '" + "jitesh.zende@t-systems.com" + "')&apiKey=VTEXGXaHe0fvMK1wS0kie7U1e4umXMNv5UM1a1UK";
      
resp = requests.get(url)
if resp.status_code != 200:
	print('Error: Rest API Error ' + str(resp.status_code))
else:
	obj = json.loads(resp.content)
#for key in obj[0]:
  #print(obj[0][key])
#print(obj[0]['id'])

#message = tracker.latest_message.get('text');
#obj = json.loads(message)
email = client_id = company_name = dept_id = dept_name = loc_id = loc_name = first_name = last_name = user_name = None;
if(obj):
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

url2 = "http://localhost:5005/conversations/" + "Amol" + "/tracker/events"
data2 = [
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
	print('Error: Rest API Amol ' + str(resp2.status_code))
else:
	obj2 = json.loads(resp2.content)
print(obj2)