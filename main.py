import pyautogui
import webbrowser
import os, sys
import subprocess
  

subprocess.check_output([webbrowser.open('vk.com')])
wh = pyautogui.size() # Obtain the screen resolution.
print(wh)
i=0
'''
for i in range(10): 
    pyautogui.move (100, 0, duration = 0.25)    # right
    pyautogui.move (0, 100, duration = 0.25)    # вниз
    pyautogui.move (-100, 0, duration = 0.25)   # влево
    pyautogui.move (0, -100, duration = 0.25) 
    i=i+1
'''
#pyautogui.doubleClick (10, 5) 
#im = pyautogui.screenshot ()
pyautogui.click (1000, 200); 
pyautogui.write ('Hello, World!')