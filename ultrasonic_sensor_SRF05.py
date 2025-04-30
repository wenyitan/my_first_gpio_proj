from gpiozero import DistanceSensor, RGBLED
from time import sleep

# Setup
# echo first, then trigger
sensor = DistanceSensor(echo=18, trigger=23, threshold_distance=0.2)
led = RGBLED(red=16, green=20, blue=21, initial_value=(0,0,0), pwm=True, active_high=False)

def led_on():
    led.color = (1,0,0)

def led_off():
    led.color = (0,0,0)

sensor.when_in_range = led_on
sensor.when_out_of_range = led_off

try:
    while True:
        distance_m = sensor.distance  # distance in meters
        distance_cm = distance_m * 100
        print(f"Distance: {distance_cm:.2f} cm")
        sleep(0.05)
        


except KeyboardInterrupt:
    print("Measurement stopped by User")