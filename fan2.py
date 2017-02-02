import RPi.GPIO as GPIO
import os
import time
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)       # Use BCM GPIO numbers
GPIO.setup(24, GPIO.OUT)
while 1==1:
	f=os.popen("/home/pi/fan/conf/temp.sh")
	for i in f.readlines():
		row=(i[0:4])
	row = float(row)
	if row > 42:
		print "HIGH - ", row
		GPIO.output(24, True)
		time.sleep(10*1)
	else:
		print "LOW - ", row
		GPIO.output(24, False)
		time.sleep(10)
