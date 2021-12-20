import requests

response=requests.get("https://www.bilibili.com/video/BV1hx411d7jb?p=2")
response.status_code
print(response.text)










