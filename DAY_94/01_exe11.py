# Exercise 11 - Drink Water Reminder

# Write a python program which reminds you of
# drinking water every hour or two. Your program can
# either beep or send desktop notifications for a
# specific operating system

import time
import win32com.client 
from plyer import notification

speaker = win32com.client.Dispatch("SAPI.SpVoice")
while True:
    speaker.Speak("Pani pelo bachha garme boht hai")
    notification.notify(
    title='Drink Water Reminder',
    message='Pani pelo bachha garmi boht hai',
    app_name='Python Notifier',
    timeout=5 # Notification stays for 10 seconds
    )
    time.sleep(3600)
    

      
    
   
