import config
import api

email = "ismailollege@gmail.com"
password = "helloworld"

response = api.Login(email, password)

print(response.get("statusCode"))

if response.get("statusCode"):
    print("YESS")
else:
    print("NOOOOOOOOOOO")