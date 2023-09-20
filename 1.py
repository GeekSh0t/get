import RPi.GPIO as GPIOi

GPIO.setmode(GPIO.BCM)
GPIO.setup(24, GPIO.OUT)
GPIO.output(24,1)
GPIO.setup(19, GPIO.IN)
while true: 
    GPIO.output (14, GPIO.input(19)

for _ in range(3):
    for i in range(8):
        GPIO.output(leds[i], 1)
        time.sleep(0.2)
        GPIO.output(leds[i], 0)