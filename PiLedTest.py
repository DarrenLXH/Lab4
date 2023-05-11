import hal_input_switch as switch
from time import sleep
import hal_led as led

def main():
    i = 0
    led.init()
    switch.init()
    while True:
        switchy = switch.read_slide_switch()
        if switchy == 1:
            led.set_output(1, 1)
            sleep(0.2)
            led.set_output(1, 0)
            sleep(0.2)
            i = 0
        else:
            while(i < 25):
                led.set_output(1, 1)
                sleep(0.1)
                led.set_output(1, 0)
                sleep(0.1)
                i += 1


if __name__ == "__main__":
    main()