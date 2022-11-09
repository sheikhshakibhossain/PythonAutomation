import os, sys, time
import pyautogui as bot

def exit_status(): # not working, have to use exception handling 
    if sys.argv[2] == "":
        quit()

def start_timer():
    i = 5
    while(i>0):
        print("Starting attack in " + str(i))
        time.sleep(1)
        os.system('clear')
        i -= 1

def send_message():
    i = 0
    while(i < int(count)):
        bot.typewrite(message)
        bot.press('enter')
        i += 1
        time.sleep(int(wait))

# execution begins from here
param = sys.argv[1:]
message = param[0]
count = param[1]
wait = param[2]

exit_status()
start_timer()
send_message()