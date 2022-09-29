# Write your code here :-)
import time
import usb_hid
import bitbangio
import board
from adafruit_mcp230xx.mcp23017 import MCP23017
from hid_gamepad import Gamepad

print("i2c and MCP Init")
try:
    i2c = bitbangio.I2C(board.GP13, board.GP12)
    mcp0 = MCP23017(i2c)
    print("-> done")
except:
    print(" initialization failure")

print("gamepad init")
gp = Gamepad(usb_hid.devices)


button_pins = (
    mcp0.get_pin(0),
    mcp0.get_pin(1),
    mcp0.get_pin(2),
    mcp0.get_pin(3),
    mcp0.get_pin(4),
    mcp0.get_pin(5),
    mcp0.get_pin(6),
    mcp0.get_pin(7),
    mcp0.get_pin(8),
    mcp0.get_pin(9),
    mcp0.get_pin(10),
    mcp0.get_pin(11),
    mcp0.get_pin(12),
    mcp0.get_pin(13),
    mcp0.get_pin(14),
    mcp0.get_pin(15),
)
print("Buttons Pins: ", gamepad_buttons)

gamepad_buttons = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16)
print("gpButtons: ", gamepad_buttons)

# Create some buttons. The physical buttons are connected
# to ground on one side and these and these pins on the other.
# button_pins = (board.D2, board.D3, board.D4, board.D5)

# Map the buttons to button numbers on the Gamepad.
# gamepad_buttons[i] will send that button number when buttons[i]
# is pushed.
# gamepad_buttons = (1, 2, 8, 15)

buttons = [digitalio.DigitalInOut(pin) for pin in button_pins]
for button in buttons:
    button.direction = digitalio.Direction.INPUT
    button.pull = digitalio.Pull.UP
# Connect an analog two-axis joystick to A4 and A5.
#ax = analogio.AnalogIn(board.A4)
#ay = analogio.AnalogIn(board.A5)

# Equivalent of Arduino's map() function.
#def range_map(x, in_min, in_max, out_min, out_max):
#    return (x - in_min) * (out_max - out_min) // (in_max - in_min) + out_min


while True:
    # Buttons are grounded when pressed (.value = False).
    for i, button in enumerate(buttons):
        gamepad_button_num = gamepad_buttons[i]
        if button.value:
            gp.release_buttons(gamepad_button_num)
            print(" release", gamepad_button_num, end="")
        else:
            gp.press_buttons(gamepad_button_num)
            print(" press", gamepad_button_num, end="")


# while True:
#   try:
#      #for x in range(16):
#     #    pin = mcp0.get_pin(x)
#    print(pin.value)
#    time.sleep(0.5)
#    print(b0.value)
#   time.sleep(0.1)
# except:
#   pass

i2c.deinit()
