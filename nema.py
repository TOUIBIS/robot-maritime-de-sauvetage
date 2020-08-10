import RPi.GPIO as GPIO
import time 

ena = 12 
steppin = 3
dirpin = 5


GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

GPIO.setup(ena,GPIO.OUT)
GPIO.setup(steppin,GPIO.OUT)
GPIO.setup(dirpin,GPIO.OUT)

GPIO.output(ena,GPIO.LOW)

try:
	GPIO.output(dirpin,GPIO.HIGH)
	for x in range (500):
		GPIO.output(steppin,GPIO.HIGH)
		print('*')
		time.sleep(0.005)
		GPIO.output(steppin,GPIO.LOW)
		time.sleep(0.005)
	GPIO.output(ena,GPIO.HIGH)
				
except KeyboardInterrupt:
    GPIO.cleanup()	

