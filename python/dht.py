import Adafruit_DHT
import RPi.GPIO as GPIO
from time import sleep

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

sensor = Adafruit_DHT.DHT11
sensor_data = 4
BLUE_PIN = 13
YELLOW_PIN = 15

GPIO.setup(BLUE_PIN, GPIO.OUT)
GPIO.setup(YELLOW_PIN, GPIO.OUT)

GPIO.output(BLUE_PIN, GPIO.LOW)
GPIO.output(YELLOW_PIN, GPIO.LOW)

while True:
    humidity, temperature = Adafruit_DHT.read(sensor, sensor_data)
    if humidity is not None and temperature is not None:
		print('Temp={0:0.1f}*C Humidity={1:0.1f}%'.format(temperature, humidity))
		if temperature < 24:
			GPIO.output(BLUE_PIN, GPIO.HIGH)
		elif temperature > 27:
			GPIO.output(YELLOW_PIN, GPIO.HIGH)
		else:
			GPIO.output(BLUE_PIN, GPIO.LOW)
			GPIO.output(YELLOW_PIN, GPIO.LOW)
    else:
        print('Failed to read. Try again!')
        
    sleep(2)
