import RPi.GPIO as GPIO          
from time import sleep

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(40,GPIO.OUT)

pwm1=GPIO.PWM(40, 50)
pwm1.start(0)


def SetAngle1(angle):
	duty = angle / 18 + 2
	pwm1.ChangeDutyCycle(duty)
	sleep(0.3)



SetAngle1(150)
	
