import subprocess

#pro2 = subprocess.Popen(["rasa", "run", "actions", "--actions", "actions"], creationflags=subprocess.CREATE_NEW_CONSOLE)
test = subprocess.Popen(["rasa", "run", "actions", "--actions", "actions"], stdout=subprocess.PIPE)
output = test.communicate()[0]

#pro2 .send_signal(signal.CTRL_BREAK_EVENT)

#subprocess.Popen("TASKKILL /F /PID {} /T".format(pro2.pid))

#os.kill(pro2.pid, signal.SIGTERM )
#os.killpg(os.getpgid(pro.pid), signal.SIGTERM)
