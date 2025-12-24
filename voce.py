import time
from djitellopy import Tello
import speech_recognition as sr # type: ignore

tello = Tello()
tello.connect()

recognizer = sr.Recognizer()  # una sola istanza

def ascolta_comando():
    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source)
        print("sono in ascolto...")
        audio = recognizer.listen(source)
    try:
        text = recognizer.recognize_google(audio, language="it-IT")
        print(text)
        return text.lower()
    except:
        print("non ho capito.")
        return ""

while True:
    comando = ascolta_comando()

    if "decolla" in comando:
        print("sto decollando")
        tello.takeoff()

    elif "atterra" in comando:
        print("sto atterrando")
        tello.land()

    elif "sinistra" in comando:
        print("sto andando a sinistra")
        tello.move_left(100)

    elif "destra" in comando:
        print("sto andando a destra")
        tello.move_right(100)
        
    elif "flip" in comando:
        print("sto facendo un flip")
        time.sleep(5)
        tello.flip("f")
        time.sleep(1)
    
    elif "stop" in comando:
        print("fine")
        tello.end()
        break