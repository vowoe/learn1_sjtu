import threading
from pynput.mouse import Button, Listener, Controller
from pynput import keyboard
import time
 
shoot = 0
scope = -1
status = 1

controller = Controller()

def mouse_click(x, y, button, pressed):
    global shoot
    global scope
    if pressed:
        if button == Button.right:
            scope = - scope
        if button == Button.left:
            shoot = 1
    if not pressed and button == Button.left:
        shoot = 0
 
def keyboard_release(key):
    global status

    if key == keyboard.Key.backspace:
        status = -status

def mouseListener():
    with Listener(on_click=mouse_click) as listener:
        listener.join()
 
def keyboardListener():
    with keyboard.Listener(
            on_release=keyboard_release) as listener:
        listener.join()
 
def main():
    threading._start_new_thread(mouseListener, ()) 
    threading._start_new_thread(keyboardListener, ())
    while 1:
        if shoot == 1 and scope == -1 and status == 1:
            time.sleep(0.05)
            controller.move(0, +10)
        elif shoot == 1 and scope == 1 and status == 1: 
            time.sleep(0.05)
            controller.move(0, +20)

if __name__ == '__main__':
    main()
