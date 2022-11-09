import os, time
import pyautogui as bot

def start_timer():
    i = 5
    while(i>0):
        print("Starting attack in: " + str(i))
        time.sleep(1)
        os.system('clear')
        i -= 1

def send_love_mesg(count, wait, babeName):
    mesg = "I love you " + babeName
    i = 0
    while (i < int(count)):
        bot.typewrite(mesg)
        bot.press("enter")
        i += 1
        time.sleep(int(wait))
    print("Done...")


babeName = input("Babe name: ")
count = input("Number of message: ")
time_stamp = input("Seconds between messages: ")

start_timer()
send_love_mesg(count, time_stamp, babeName)
