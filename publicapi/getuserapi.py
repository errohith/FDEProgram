import requests

url = "https://jsonplaceholder.typicode.com/users"

response = requests.get(url)

print(response.status_code)
print(response.json())

users = response.json()
for user in users:
    print("Username:", user["username"])
    print("Email:", user["email"])
    print("Company Name:", user["company"]["name"])
    print("-------------------------")


import requests
import re

url = "https://jsonplaceholder.typicode.com/users"

response = requests.get(url)

assert response.status_code == 200
users = response.json()

for user in users:

    username = user["username"]
    email = user["email"]
    company = user["company"]["name"]
    phone = user["phone"]

    match = re.search(r"x(\d+)", phone)

    print("Username:", username)
    print("Email:", email)
    print("Company Name:", company)
    print("Phone:", phone)

    if match:
        extension = match.group(1)

        if len(extension) > 6:
            print("Extension:", extension)
        else:
            print("Extension: Less than or equal to 4 digits")
    else:
        print("Extension: Not available")

    print("-----------------------------")