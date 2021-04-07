import sys
import pyautogui as p
import time as t
import keyboard
import time
import os
import psutil
from threading import Thread
print("Credits: DSP")
current_system_pid = os.getpid()
p.FAILSAFE = True
def stop():
    while True:
        x = keyboard.read_key()
        if(x == '0'):
            ThisSystem = psutil.Process(current_system_pid)
            ThisSystem.terminate() 
def skip():
    while True:
        print("Loading......")
        #Click Enter Button
        p.click(913,687)
        #Choosing 'I have no subject Knowledge' option
        p.press('left')
        #Click Submit
        p.click(1182,582)
        time.sleep(10)       
p1 = Thread(target=skip)
p2 = Thread(target=stop)
p1.start()
p2.start()



    
   
