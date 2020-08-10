import RPi.GPIO as GPIO          
from time import sleep

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(32,GPIO.OUT)

pwm2=GPIO.PWM(32, 50)
pwm2.start(0)

def SetAngle2(angle):
	duty = angle / 18 + 2
	pwm2.ChangeDutyCycle(duty)
	sleep(0.5)

while(1):
	SetAngle2(90)
