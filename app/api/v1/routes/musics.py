import base64
import requests
from config import CLIENT_ID, CLIENT_SECRET

auth_string = f"{CLIENT_ID}:{CLIENT_SECRET}"
base64_auth_string = base64.b64encode(auth_string.encode('ascii')).decode('ascii')

auth_options = {
    "grant_type": "client_credentials",
}

headers = {
    "Authorization": f"Basic {base64_auth_string}",
    "Content-Type": "application/x-www-form-urlencoded",
}

url = "https://accounts.spotify.com/api/token"

response = requests.post(url, headers=headers, data=auth_options)

if response.status_code == 200:
    print(response)
    print(response.json())
    token = response.json()["access_token"]
    print(token)
else:
    print(f"Error: {response.status_code}")
