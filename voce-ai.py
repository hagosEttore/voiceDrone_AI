import time
from djitellopy import Tello
import speech_recognition as sr # type: ignore
import re

tello = Tello()
tello.connect()
print("Battery:", tello.get_battery())


recognizer = sr.Recognizer()

def ascolta_comando():
    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source)
        print("sono in ascolto...")
        audio = recognizer.listen(source)
    try:
        text = recognizer.recognize_google(audio, language="it-IT")
        print("comando:", text)
        return text.lower()
    except:
        print("non ho capito.")
        return ""

def interpreta_con_ai(testo):
    direzioni = {
        "sinistra": "left",
        "destra": "right",
        "avanti": "forward",
        "indietro": "back",
        "su": "up",
        "giù": "down"
    }

    numero = re.search(r"\d+", testo)
    distanza = int(numero.group()) if numero else 50

    for parola, comando in direzioni.items():
        if parola in testo:
            return comando, distanza

    return None, None

def esegui_comando(direzione, distanza):
    if direzione == "left":
        tello.move_left(distanza)
    elif direzione == "right":
        tello.move_right(distanza)
    elif direzione == "forward":
        tello.move_forward(distanza)
    elif direzione == "back":
        tello.move_back(distanza)
    elif direzione == "flip":
        tello.flip()



while True:
    comando = ascolta_comando()

    if "decolla" in comando:
        tello.takeoff()

    elif "atterra" in comando:
        tello.land()

    elif "stop" in comando:
        tello.end()
        break

    else:
        direzione, distanza = interpreta_con_ai(comando)
        if direzione:
            print(f"AI: {direzione} di {distanza} cm")
            esegui_comando(direzione, distanza)
