import os
#os.system("pwd")
#os.system("rasa run -m ./models --enable-api --endpoints endpoints.yml --cors '*' --debug")
#os.system("rasa run actions --actions actions")

#from subprocess import call
#call(["rasa", "run", "-m", "./models", "--enable-api", "--endpoints", "endpoints.yml", "--cors", "*", "--debug"])

"""
#!/usr/bin/env python
#Show messages in two new console windows simultaneously
import sys
import platform
from subprocess import Popen

messages = 'This is Console1', 'This is Console2'

# define a command that starts new terminal
if platform.system() == "Windows":
    new_window_command = "cmd.exe /c start".split()
else:  #XXX this can be made more portable
    new_window_command = "x-terminal-emulator -e".split()

# open new consoles, display messages
echo = [sys.executable, "-c",
        "import sys; print(sys.argv[1]); input('Press Enter..')"]
processes = [Popen(new_window_command + echo + [msg])  for msg in messages]

# wait for the windows to be closed
for proc in processes:
    proc.wait()

"""

import os                                                                       
from multiprocessing import Pool                                                
                                                                                                                                                                
processes = ('rasa-run-server.py', 'rasa-run-actions.py')

def run_process(process):                                                             
    os.system('python {}'.format(process))
                                                                                    
pool = Pool(processes=2)                                                        
pool.map(run_process, processes)   