import os, sys, time
import pyautogui as bot

def exit_status(firstParam): # not working, have to use exception handling 
    if firstParam == "":
        quit()

def start_timer():
    i = 5
    while(i>0):
        os.system('clear')
        print("Starting attack in " + str(i))
        time.sleep(1)
        i -= 1
    os.system('clear')

def send_message():
    print("running your attack ...")
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

exit_status(param[0])
start_timer()
send_message()