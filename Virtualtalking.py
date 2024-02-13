# Virtual Talking Friend Using Pip Package Library
import pyttsx3
vtf = pyttsx3.init()
rate = vtf.getProperty('rate')  
vtf.setProperty('rate', 180)    

def vtf_speak(audio):
    print("speaking....")
    vtf.say(audio)
    vtf.runAndWait()

txt="Hello , i am virtual talking friend"
vtf_speak(txt)


while txt!="bye":
    txt1=input("what should i say :")
    txt=txt1.lower()
    if txt1!="bye":
        vtf_speak(txt)
    else:
        vtf_speak("see you again friend,that was nice talking you")

