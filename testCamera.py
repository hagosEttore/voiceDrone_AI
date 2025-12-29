from djitellopy import tello
import cv2

drone = tello.Tello()
drone.connect()
print(f"Battery: {drone.get_battery()}%")

drone.streamon()

while True:
    frame = drone.get_frame_read().frame
    frame = cv2.resize(frame, (360, 240))
    cv2.imshow("Drone Camera", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break