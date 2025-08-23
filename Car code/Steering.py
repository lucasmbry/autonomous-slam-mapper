from machine import PWM, Pin
import time

# Set the GPIO pin number (based on the connection in step 2)
servo_pin = machine.Pin(0)
# Set the PWM frequency (50Hz is common for servos)
pwm_freq = 50

# Create a PWM object with the specified pin and frequency
pwm = PWM(servo_pin)
pwm.freq(pwm_freq)

# Main loop

pwm.duty_ns(1500000)
time.sleep(0.1)

pwm.duty_ns(700000)
time.sleep(0.1)
