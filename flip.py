from djitellopy import Tello
import time

# Inizializza il drone
tello = Tello()
tello.connect()
print("Batteria:", tello.get_battery(), "%")

print("sto decollando")
tello.takeoff()
time.sleep(5)  # piccolo ritardo per stabilizzarsi

# Flip avanti
print("sto facendo un flip")
tello.flip("f")
time.sleep(1)  # piccolo ritardo

# Atterraggio
print("sto atterrando")
tello.land()