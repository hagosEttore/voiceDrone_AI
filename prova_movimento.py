import keyboard
while True:
    print("premi un tasto per muoverti")
    keyboard.wait("up")
    x = 0
    while keyboard.is_pressed("a"):
        print("a")
    keyboard.wait("w")
    while keybopard.is_pressed("w"):
        print("w")
    keyboard.wait("right")
    while keyboard.is_pressed("up"):
        print("ok")
    

    keyboard.wait("q")
    if(keyboard.is_pressed("q")):
        print("q")
        break




# if keyboard.is_pressed('a'):
#     print("hai premuto il tasto a!!")