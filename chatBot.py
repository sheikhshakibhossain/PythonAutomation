import os, time
import pyautogui as bot

i = 5
while(i>0):
    print("Starting attack in: " + str(i))
    time.sleep(1)
    os.system('clear')
    i -= 1

babeName = "my queen"
mesg = "I love you " + babeName
wait = 3 # seconds
count = 1

i = 0
while (i < count):
    bot.typewrite(mesg)
    bot.press("enter")
    i += 1
    time.sleep(wait)
print("Done...")
