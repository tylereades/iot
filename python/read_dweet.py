import urllib2
import json

myDweet = 'http://dweet.io/get/dweets/for/LU-CSC49008-ourexample'
response = urllib2.urlopen(myDweet)
print(response)
print()
html = response.read()
print(html)
print()
data = json.loads(html)
for obv in data['with']:
	print(obv['content']['humidity'])
