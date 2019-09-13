import subprocess
import schedule
import time, datetime

def terminate_subprocess(t,pro):
	print(t)
	print("Stopping Server on", datetime.datetime.now())
	pro.terminate()
	time.sleep(10)
	start_subprocess()
	return

def start_subprocess():
	print("Starting Server on", datetime.datetime.now())
	pro = subprocess.Popen(["rasa", "run", "-m", "./models", "--enable-api", "--endpoints", "endpoints.yml", "--cors", "*", "--debug", "--credentials","credentials.yml"], stdout=subprocess.PIPE)
	return pro

def start_action_server():
	print("Starting Action Server in New Console")
	pro2 = subprocess.Popen(["rasa", "run", "actions", "--actions", "actions"], creationflags=subprocess.CREATE_NEW_CONSOLE)
	return pro2

pro = start_subprocess()
pro2 = start_action_server()

schedule.every().day.at("16:20").do(terminate_subprocess,'Commencing Scheduled Restart of Server',pro)

while True:
	schedule.run_pending()
	time.sleep(60)


