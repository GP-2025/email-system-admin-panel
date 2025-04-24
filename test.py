import config
import api

email = "ismailcollege@gmail.com"
password = "helloworld"

response = api.Login(email, password)
token = response["accessToken"]

data={
    "name": "Arts and Sciences",
    "abbreviation": "AC"
}

new = api.AddCollege(data, token)
print(new)