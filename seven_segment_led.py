### pin 1 - gpio 25 - E
### pin 2 - gpio 8 - D
### pin 3 - gpio 7 - decimal
### pin 4 - gpio 16 - C
### pin 5 - gpio 20 - G
### pin 7 - gpio 21 - B
### pin 8 - gpio 5 - dig3
### pin 9 - gpio 6 - dig2
### pin 10 - gpio 13 - F
### pin 11 - gpio 19 - A
### pin 12 - gpio 26 - dig1
from gpiozero import LED
from time import sleep

segments = {
    'a': LED(19),
    'b': LED(21),
    'c': LED(16),
    'd': LED(8),
    'e': LED(25),
    'f': LED(13),
    'g': LED(20),
    ".": LED(7)
}

number_to_segments = {
    "0": ['a', 'b', 'c', 'd', 'e', 'f'],
    "1": ['b', 'c'],
    "2": ['a', 'b', 'd', 'e', 'g'],
    "3": ['a', 'b', 'c', 'd', 'g'],
    "4": ['b', 'c', 'f', 'g'],
    "5": ['a', 'c', 'd', 'f', 'g'],
    "6": ['a', 'c', 'd', 'e', 'f', 'g'],
    "7": ['a', 'b', 'c'],
    "8": ['a', 'b', 'c', 'd', 'e', 'f', 'g'],
    "9": ['a', 'b', 'c', 'd', 'f', 'g'],
    "A": ['a', 'b', 'c', 'e', 'f', 'g'],
    "B": ['a', 'b', 'c', 'd', 'e', 'f', 'g'],
    "C": ['a', 'e', 'f', 'd'],
    "D": ['a', 'b', 'c', 'd', 'e', 'f'],
    "E": ['a', 'e', 'f', 'd', 'g'],
    "F": ['a', 'e', 'f', 'g'],
    "G": ['a', 'c', 'd', 'e', 'f', 'g'],
    "H": ['b', 'c', 'f', 'e', 'g'],
    "I": ['b', 'c',],
    "J": ['a', 'b', 'c', 'd'],
    ".": ['.']
}

digits = [LED(26), LED(6), LED(5)]
# while True:
    # led1.on()
    # led2.off()
    # led3.off()

    # for i in number_to_segments.values():
    #     for j in i:
    #         segments[j].on()
    #     time.sleep(1)
    #     for segment in segments.values():
    #         segment.off()

def light_number_on_digit(digit, number):
    for dig in digits:
        dig.on()
    digits[digit].off()
    for segment in segments.values():
        segment.off()
    for segment in number_to_segments[number]:
        segments[segment].on()

def display_number(number):
    digits_list = [i for i in str(number).zfill(3)]  # Ensure 3 digits
    # Loop through digits and display
    for i in range(100):
        light_number_on_digit(i%3, digits_list[i%3])
        sleep(0.005)  # Small delay to simulate multiplexing

try:
    for i in "ABCDEFGHIJ":
        display_number(i)
except KeyboardInterrupt:
    print("Program stopped.")