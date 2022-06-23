#!/usr/bin

import requests 
u = "http://165.227.106.113/post.php"

payload = {
		"username": "admin",
		"password": "71urlkufpsdnlkadsf"
		}
data = requests.post(url = u, data = payload)

print(data.text)