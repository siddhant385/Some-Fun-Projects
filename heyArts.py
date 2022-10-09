import ctypes
import pyttsx3
import requests
import time
import os


class heyArts:
    def __init__(self):
        self.imagepath = os.path.abspath("wallpaper.jpg")
        self.imageurl = "https://raw.githubusercontent.com/siddhant385/Python-Games/main/resources/wallpaper.txt"
    
    def wallpaper(self):
        #print(self.imagepath)
        SPI_SETDESKWALLPAPER = 20 
        ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, self.imagepath , 2)

    def geturl(self):
        try:
            response = requests.get(self.imageurl)
            return response.content.decode("utf-8")
        except:
            return "Error Failed to connect"

    def speak(self,audio):
        engine = pyttsx3.init()
        voices = engine.getProperty('voices')
        engine.setProperty('voice', voices[0].id)
        engine.setProperty('rate',100)
        engine.say(audio) 
        engine.runAndWait()

    def downloadwallapaper(self,url):
        response = requests.get(url)
        if response.status_code == 200:
            with open("wallapaper.jpg", 'wb') as f:
                f.write(response.content)
        f.close()

    def main(self):
        try:
            if not self.geturl().startswith("http"):
                url = "https://images.pexels.com/photos/1766838/pexels-photo-1766838.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1"
            else:
                url = self.geturl()
            self.downloadwallapaper(url)
            self.speak("downloaded wallpaper")
            #print("downloaded wallpaper")
            self.wallpaper()
            #print("wallpaper changed")
            self.speak("wallpaper changed")
        except Exception as e:
            print(e)
            pass

s = heyArts()
s.main()
while True:
    s.speak("Hey Arts")
    #print("hey arts")
    time.sleep(5)