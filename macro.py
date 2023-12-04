import sys
import keyboard
import pygetwindow
import getkey
import pymouse
from pykeyboard import PyKeyboard

os = sys.platform

#if keyboard.is_pressed('space'):
#    PyKeyboard.press_keys(['rightshift', 'delete', 'r'])
if os == 'darwin':
    windows_open = pygetwindow.getAllTitles()

if 'Stardew Valley ' in windows_open:
    while True:
        event = keyboard.read_event()
        if event.event_type == keyboard.KEY_DOWN and event.name == 'space':
            keyboard.send('right_shift+r+del')




