import config
import api

email = "ismailcollege@gmail.com"
password = "helloworld"

response = api.Login(email, password)
token = response["accessToken"]

new = api.GetCollegeById(7, token)
print(new)