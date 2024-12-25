import time
import win32api
import psutil
import AppOpener
import pyautogui

from AppOpener import open,close
from datetime import datetime, timedelta

pyautogui.FAILSAFE = False
i=108
def idle_check():
    global i
    while i>3:
        a=win32api.GetLastInputInfo() 
        time.sleep(1800) #provide the time in between checks(in secs) , 30 mins by default 
        b=win32api.GetLastInputInfo()
        if a==b:
            
            while i > 3:
                if ("Valorant.exe" in (i.name() for i in psutil.process_iter()))==True: #checks if valorant is open
                    #print("Application Online")
                    # Continue checking for idle state
                    idle_check()               
                else:
                    #print("Application Offline")
                    i = 2
                    
                    break    
        else:
            pass
            #print("Not idle")

def open_application():
    # First check if Application is already running
    if "Valorant.exe" not in (i.name() for i in psutil.process_iter()):
        open("Valorant", match_closest=True)
        
    else:
        pass

def store_screenshot():
    try:
        #print("Moving cursor to position...")
        pyautogui.moveTo(146, 866, 2)
        pyautogui.click()
        time.sleep(2) #waits 2 sec before taking picture to avoid accidental loading image
        
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")  # generate timestamp
        screenshot_filename = f"screenshot_{timestamp}.png"     # unique filename
        screenshot = pyautogui.screenshot(screenshot_filename)
        
    except Exception as e:
        pass
        

def close_application(app_name):
    for process in psutil.process_iter():
        if app_name.lower() in process.name().lower(): #terminating the application
            process.terminate()
            
            
def time_late():
    idle_check()
    cur_time=datetime.now() #checks time when idle state is confirmed
    #print(f'starttime: {cur_time}')
    open_application()
    time.sleep(80)
    store_screenshot()
    close_application("Valorant")
    current_time=datetime.now()  #checks time when screenshot has been saved and application closed
    #print(f'end time : {current_time}')
    time_diff = current_time-cur_time
    #print(f'time diff is : {time_diff}')
    if time_diff > timedelta(seconds=86400):
       time_late()
    else:
       wait_time = (timedelta(seconds=86400) - time_diff).total_seconds()
       time.sleep(wait_time)
       #print("now open again")
       time_late()
    
time_late()
