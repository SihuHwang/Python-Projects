import pyautogui
import webbrowser
import time
from datetime import datetime

while True:
    now =datetime.now()

    if now.strftime("%H%M%S") == "184730":
        webbrowser.get("C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s").open_new(
        "https://zoom.us")

        time.sleep(7)
        pyautogui.click(1435, 150)
        time.sleep(6)
        pyautogui.click(945, 750)
        time.sleep(6)
        pyautogui.click(916, 590)

    if now.strftime("%H%M%S") == "184800":
        webbrowser.get("C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s").open_new(
        "https://zoom.us")


    break









        # pyautogui.hotkey('alt', 'v')
        # pyautogui.hotkey('alt', 'a')


