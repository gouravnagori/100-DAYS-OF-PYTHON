
import win32com.client

shoutout = ["Arpan", "Agnishwar", "Swapnil","Aritra", "Arnab"]

speaker = win32com.client.Dispatch("SAPI.SpVoice")

for name in shoutout:
    s = name
    speaker.Speak( f"Shoutout to {name} ")
