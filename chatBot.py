import time
import pyautogui as bot

print("Starting attack in: ")
i = 5
while(i>0):
    print(i)
    time.sleep(1)
    i -= 1

babeName = "Sauda"
mesg = "I love you " + babeName
wait = 5 # seconds
count = 5
i = 0
while (i < count):
    bot.typewrite(mesg)
    bot.press("enter")
    i += 1
    time.sleep(wait)
