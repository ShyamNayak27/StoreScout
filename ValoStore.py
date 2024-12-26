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
            print("Idle")
            #print(type("Application.exe" in (i.name() for i in psutil.process_iter())))
            while i > 3:
                if ("Valorant.exe" in (i.name() for i in psutil.process_iter()))==True:
                    #print("Application Online")
                    # Continue checking for idle state
                    idle_check()               
                else:
                    print("Application Offline")
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
        print("Working...")


def store_screenshot():
    try:
        print("Moving cursor to position...")
        pyautogui.moveTo(146, 866, 2)
        pyautogui.click()
        time.sleep(2)
        print("Taking screenshot...")
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")  # generate timestamp
        screenshot_filename = f"screenshot_{timestamp}.png"     # unique filename
        screenshot = pyautogui.screenshot(screenshot_filename)
        print(f"Screenshot saved as '{screenshot_filename}'.")
    except Exception as e:
        pass
        print(f"Error while taking screenshot: {e}")

def close_application(app_name):
    for process in psutil.process_iter():
        if app_name.lower() in process.name().lower():
            process.terminate()
            print(f"{app_name} has been closed.")
            
def time_late():
    idle_check()
    cur_time=datetime.now()
    print(f'starttime: {cur_time}')
    open_application()
    time.sleep(100)
    store_screenshot()
    close_application("Valorant")
    current_time=datetime.now()
    print(f'end time : {current_time}')
    time_diff = current_time-cur_time
    print(f'time diff is : {time_diff}')
    if time_diff > timedelta(seconds=86400):
       time_late()
    else:
       wait_time = (timedelta(seconds=86400) - time_diff).total_seconds()
       time.sleep(wait_time)
       print("Opening...")
       time_late()
    
time_late()
