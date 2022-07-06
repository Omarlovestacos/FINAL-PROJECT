from microbit import *
from ultrasonic import Ultrasonic

ultrasonic_sensor = Ultrasonic()
pin0.set_analog_period(0)
ultrasonic_sensor = Ultrasonic()
pin0.set_analog_period(20)

while True:
    distance_value = ultrasonic_sensor.measure_distance_cm()
    if distance_value <= 20:
        pin2.write_digital(1)
    else:
        pin2.write_digital(0)

    '''motion = pin1.read_digital()
    if motion == 1 and  < 15:
        pin1.write_digital(1)
        pin16.write_digital(1)
    else:
        pin16.write_digital(0)
        pin1.write_digital(0)
'''

    pin0.write_analog(1023 * 1.0 / 20)
    sleep(2000)
    pin0.write_analog(1023 * 2.0 / 20)
    sleep(2000)
    pin0.write_analog(1023 * 1.5 / 20)
    sleep(2000)
    pin0.write_analog(1023 * 2.5 / 20)
