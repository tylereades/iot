import Adafruit_DHT
import urllib2
import RPi.GPIO as GPIO
from time import sleep

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

BUTTON_PIN = 7
GPIO.setup(BUTTON_PIN, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

LED_PIN = 11

GPIO.setup(LED_PIN, GPIO.OUT)

#GPIO.output(LED_PIN, GPIO.HIGH)
led_on = True if GPIO.input(LED_PIN) == 1 else False


while True:
	readValue = GPIO.input(BUTTON_PIN)
	
	if readValue == GPIO.HIGH and led_on:
		GPIO.output(LED_PIN, GPIO.LOW)
		led_on = False
	elif readValue == GPIO.HIGH and not led_on:
		GPIO.output(LED_PIN, GPIO.HIGH)
		led_on = True
		
	print(readValue)
		
	sleep(.2)
