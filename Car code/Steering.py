# Rui Santos & Sara Santos - Random Nerd Tutorials
# Complete project details at https://RandomNerdTutorials.com/raspberry-pi-pico-servo-motor-micropython/

from machine import Pin, PWM
from time import sleep
import keyboard

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

while True:
    if keyboard.is_pressed("a"):
        servo.duty_u16(min_duty)
    if keyboard.is_pressed("d"):
        servo.duty_u16(max_duty)



servo.deinit()
"""
try:
    while True:
        #Servo at 0 degrees
        servo.duty_u16(min_duty)
        sleep(2)
        #Servo at 90 degrees
        servo.duty_u16(half_duty)
        sleep(2)
        #Servo at 180 degrees
        servo.duty_u16(max_duty)
        sleep(2)    
      
except KeyboardInterrupt:
    print("Keyboard interrupt")
    # Turn off PWM 
    servo.deinit()
"""