import config
import api

email = "ismailcolege@gmail.com"
password = "helloworld"

response = api.Login(email, password)

print(response)
# if response:
# else:
#     print("NOOOOOOOOOOO")