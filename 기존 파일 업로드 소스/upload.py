import requests

url = 'http://127.0.0.1/upload.php'
files={'myfile': open('c.txt','rb')}
r=requests.post(url,files=files)
print(r)