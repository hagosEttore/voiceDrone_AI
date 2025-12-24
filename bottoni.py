from flask import Flask, redirect, url_for
from djitellopy import Tello
import time

app = Flask(__name__) 

tello = Tello()
tello.connect()

@app.route('/')
def bottoni():
    
    return '''
    <html>
    <head>
        <title>pulsanti decolla e atterra</title>
    </head>
    <body>
    <form method="post" action="/decolla">
        <input type="submit" value="decolla"></input>
    </form>
    <form method="get" action="/atterra">
        <input type="submit" value="atterra"></input>
    </form>
    <form method="get" action="/destra">
        <input type="submit" value="destra"></input>
    </form>
    <form method="get" action="/sinistra">
        <input type="submit" value="sinistra"></input>
    </form>
    <form method="get" action="/flip">
        <input type="submit" value="flip"></input>
    </form>
    </body>
</html>
    '''
    return html_form

@app.route('/decolla', methods = ["POST"])
def decolla():
    try:
        tello.takeoff()
        return "Drone decollato!"
    except Exception as e:
        print(f"Errore: {e}")
    
    return redirect(url_for("bottoni"))

@app.route('/atterra')
def atterra():
    try:
        tello.land()
        return "Drone atterrato!"
    except Exception as e:
        return f"Errore: {e}"

@app.route('/destra')
def destra():
    try:
        tello.move_right(100)
        return "Drone mosso a destra!"
    except Exception as e:
        return f"Errore: {e}"
    
@app.route('/sinistra')
def sinistra():
    try:
        tello.move_left(100)
        return "Drone mosso a sinistra!"
    except Exception as e:
        return f"Errore: {e}"

@app.route('/flip')
def flip():
    try:
        print("Drone sta facendo un flip!")
        time.sleep(5)
        tello.flip("f")
        time.sleep(1)
    except Exception as e:
        return f"Errore: {e}"
       
app.run(port=5001)
    
    
    
