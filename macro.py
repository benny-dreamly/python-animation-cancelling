import sys
import keyboard
import pygetwindow

os = sys.platform

if os == 'darwin':
    windows_open = pygetwindow.getAllTitles()
    if 'Stardew Valley ' in windows_open:
        while True:
            event = keyboard.read_event()
            if event.event_type == keyboard.KEY_DOWN and event.name == 'space':
                keyboard.send('right_shift+r+del')
            if event.event_type == keyboard.KEY_DOWN and event.name == 'delete':
                keyboard.send('space')
if os == ('win32'):
    windows_open = pygetwindow.getAllTitles()
    if 'SMAPI ' or 'Stardew Valley' in windows_open:
        while True:
            event = keyboard.read_event()
            if event.event_type == keyboard.KEY_DOWN and event.name == 'space':
                keyboard.send('right_shift+r+del')
            if event.event_type == keyboard.KEY_DOWN and event.name == 'delete':
                keyboard.send('space')






