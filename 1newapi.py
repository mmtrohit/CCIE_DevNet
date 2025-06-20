import requests
url="https://postman-echo.com/post"
# querystring={"test":"123"}
payload="Hello Devnet"
header ={"content-type":"text/plain"}
response=requests.request("POST",url,data=payload,headers=header)
print(response.text)
print(type(response))