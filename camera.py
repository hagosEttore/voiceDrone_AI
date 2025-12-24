from djitellopy import tello
import cv2
import time

me = tello.Tello()
me.connect()
print("Battery:", me.get_battery())

# Start video stream
me.streamon()

# Wait for video to initialize
time.sleep(2)

frame_read = me.get_frame_read()

while True:
    frame = frame_read.frame

    # Check if frame is valid
    if frame is None:
        print("⚠ No frame received yet...")
        time.sleep(0.05)
        continue

    frame = cv2.resize(frame, (360, 240))
    cv2.imshow("Tello Camera", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

me.streamoff()
cv2.destroyAllWindows()