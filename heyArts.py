import struct
import ctypes
import pyttsx3
import requests
import time
import os


class heyArts:
    def __init__(self):
        self.path = os.getcwd()+"\\wallapaper.png"
        print(self.path)
        self.imageurl = "https://raw.githubusercontent.com/siddhant385/Python-Games/main/resources/wallpaper.txt"
    
    def is_64bit_windows(self):
        """Check if 64 bit Windows OS"""
        return struct.calcsize('P') * 8 == 64

    def changeBG(self):
        """Change background depending on bit size"""
        if self.is_64bit_windows():
            ctypes.windll.user32.SystemParametersInfoW(20, 0, self.path, 3)
        else:
            ctypes.windll.user32.SystemParametersInfoA(20, 0, self.path, 3)



    def geturl(self):
        try:
            response = requests.get(self.imageurl)
            return response.content.decode("utf-8")
        except:
            return "Error Failed to connect"

    def speak(self,audio):
        engine = pyttsx3.init()
        voices = engine.getProperty('voices')
        engine.setProperty('voice', voices[1].id)
        engine.setProperty('rate',100)
        engine.say(audio) 
        engine.runAndWait()

    def downloadwallapaper(self,url):
        response = requests.get(url)
        print(response.status_code)
        if response.status_code == 200:
            with open("wallapaper.png", 'wb') as f:
                f.write(response.content)
                f.close()
        else:
            print("Error")

    def main(self):
        try:
            if self.geturl().startswith("http"):
                url = "https://raw.githubusercontent.com/siddhant385/Python-Games/main/resources/wallpaper.png"
            else:
                url = self.geturl()
                print(url)
            self.downloadwallapaper(url)
            self.speak("downloaded wallpaper")
            print("downloaded wallpaper")
            self.changeBG()
            print("wallpaper changed")
            self.speak("wallpaper changed")
        except Exception as e:
            print(e)
            pass

s = heyArts()
s.main()
count = 0
while count < 10:
    s.speak("Hey Arts")
    #print("hey arts")
    time.sleep(3)
    count += 1
