# import base64
import requests
import os

from app import logger
from config import CLIENT_ID, CLIENT_SECRET, TOKEN


class Token:
    def __init__(self):
        self.auth_options = f"grant_type=client_credentials&client_id={CLIENT_ID}&client_secret={CLIENT_SECRET}"

        self.headers = {
            # "Authorization": f"Basic {base64_auth_string}",
            "Content-Type": "application/x-www-form-urlencoded",
        }

        self.url = "https://accounts.spotify.com/api/token"

    @staticmethod
    def get_actual_token():
        return os.environ['TOKEN'] or TOKEN

    def get_new_token(self):
        response = requests.post(self.url, headers=self.headers, data=self.auth_options)

        if response.status_code == 200:
            new_token = response.json()["access_token"]
            os.environ["TOKEN"] = new_token
            return new_token
        else:
            logger(f"Error: {response.status_code} - {response.json()}")
            raise Exception(response.json())
