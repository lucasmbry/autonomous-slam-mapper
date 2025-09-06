# Rui Santos & Sara Santos - Random Nerd Tutorials
# Complete project details at https://RandomNerdTutorials.com/raspberry-pi-pico-servo-motor-micropython/

from machine import Pin, PWM
import time

# Set up PWM Pin for servo control
servo_pin = machine.Pin(0)
servo = PWM(servo_pin)

#Set PWM frequency
frequency = 50
servo.freq (frequency)

# Set Duty Cycle for Different Angles
min_duty = 1800 # Left
half_duty = 3700 # Forward
max_duty = 5700 # Right

# Define functions to turn the servo
def left():
    servo.duty_u16(min_duty)
def middle():
    servo.duty_u16(half_duty)
def right():
    servo.duty_u16(max_duty)

# Set up buttons
buttonLeft = Pin(1, Pin.IN, Pin.PULL_DOWN)
buttonRight = Pin(2, Pin.IN, Pin.PULL_DOWN)

# Main loop
while True:
    if buttonLeft.value() == 1 and buttonRight.value() == 0:
        left()
    elif buttonRight.value() == 1 and buttonLeft.value() == 0:
        right()
    else:
        middle()



