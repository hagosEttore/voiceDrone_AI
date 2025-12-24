from flask import Flask
from djitellopy import Tello

app = Flask(__name__)
tello = Tello()
tello.connect()

@app.route("/decolla")
def decolla():
    try:
        tello.takeoff()
        return "Drone decollato!"
    except Exception as e:
        return f"Errore: {e}"

if __name__ == '__main__':

    app.run('127.0.0.1', 5000, debug=True)
