import urllib2
from random import randint
import time

while True:
	num = randint(1, 32)
	humidity = randint(1, 100)
	myDweet = 'http://dweet.io/dweet/for/LU-CSC49008-ourexample?temp={}&humidity={}'.format(num, humidity)
	response = urllib2.urlopen(myDweet)
	html = response.read()
	print(html)
	time.sleep(1)
