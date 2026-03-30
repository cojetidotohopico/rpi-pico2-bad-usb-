import time
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruti_hid.keycode import Keycode
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS

kbd = Keyboard(usb_hid.devices)
layout = KeyboardLayoutUS(kbd)

time.sleep(3)

kbd.press(Keycode.GUI, Keycode.R)
kbd.release_all()
time.sleep(0.5)

layout.write("shutdown /s /t 0")
time.sleep(0.2)

kbd.send(Keycode.ENTER)