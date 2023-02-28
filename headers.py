'''
solution for medium 2 - need to set some special headers
'''
import requests

payload_data = {
    "user_id": "bingus",
    "role": "admin",
    "nickname": "Jess"
}

data = requests.get("http://localhost:9888/jwt", headers={
                    "x-access-token": "bingus"})

print(data.text)
