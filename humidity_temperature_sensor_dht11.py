### DHT 11
# Sensor type (DHT11) and GPIO pin number
import board
import adafruit_dht
from time import sleep
from gpiozero import RGBLED

# Use the correct GPIO pin here (e.g., D4 is GPIO4)
dht_device = adafruit_dht.DHT11(board.D12)


led = RGBLED(red=16, green=20, blue=21, initial_value=(0,0,0), pwm=True, active_high=False)

try:
    while True:
        try:
            temperature_c = dht_device.temperature
            humidity = dht_device.humidity
            if temperature_c is not None and humidity is not None:
                print(f"Temp: {temperature_c:.1f}°C    Humidity: {humidity:.1f}%")
                if temperature_c >= 30 or humidity >= 70:
                    led.blink(1, 1, 0.5, 0.5, on_color=(0.5, 0.1, 0), off_color=(0, 0, 0))
                    # led.pulse(1, 1, n = 5, on_color=(0.5, 0.9, 1), off_color=(1,1,1))
                else:
                    led.color = (0,0,0)
            else:
                print("Sensor read failed. Trying again...")

        except RuntimeError as e:
            print(e)

        sleep(2)

except KeyboardInterrupt:
    print("Stopped by User")

finally:
    dht_device.exit()

