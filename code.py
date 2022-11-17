# Write your code here :-)
from time import sleep
import usb_hid
import digitalio
import bitbangio
import wws_74hc165
import board
from hid_gamepad import Gamepad

print("---------- GamePad USB HID Init ----------")
initialized = False

while not initialized:
    try:
        gp = Gamepad(usb_hid.devices)
        initialized = True
        print("-> Initialized")
    except:
        print("-> Initialization failure, retrying...")
    sleep(.5)


isr_latch_pin = digitalio.DigitalInOut(board.GP5)
spi = bitbangio.SPI(clock=board.GP2, MOSI=board.GP3, MISO=board.GP4)

SAMPLE_RATE = 0.2
SHIFT_REGISTERS_NUM = 1

isr = wws_74hc165.ShiftRegister74HC165(spi, isr_latch_pin, SHIFT_REGISTERS_NUM)

gp.reset_all()

def read_single_inputs():
    # Input pin definitions (pin references)
    # Buttons are grounded when pressed (.value = False).
    for pin in range(0,7):
        gamepad_button_num = pin + 1;
        pinb = isr.get_pin(pin).value
        if pinb == False:
            gp.release_buttons(gamepad_button_num)
            print("Rel:", gamepad_button_num, end=" ")
        else:
            gp.press_buttons(gamepad_button_num)
            print("Press:", gamepad_button_num, end=" ")
    print("")


# Main
print("Starting program")

while True:
    read_single_inputs()
    sleep(0.2)








