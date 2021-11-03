import pyautogui
import time

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


print(bcolors.OKGREEN + '''
   _____                       ____        _   
  / ____|                     |  _ \      | |  
 | (___  _ __   __ _ _ __ ___ | |_) | ___ | |_ 
  \___ \| '_ \ / _` | '_ ` _ \|  _ < / _ \| __|
  ____) | |_) | (_| | | | | | | |_) | (_) | |_ 
 |_____/| .__/ \__,_|_| |_| |_|____/ \___/ \__|
        | |                                    
        |_|                                    


''')
pyautogui.click
msg = input("Enter the message in qwerty: ")
n = input("How many times ? : ")
count = 5
while(count != 0):
  print("Countdown: " + str(count))
  time.sleep(1)
  count -= 1
print("Bombing...")
for i in range(0,int(n)):
  pyautogui.typewrite(msg + '\n')