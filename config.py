import os
import logging

from dotenv import load_dotenv
from os.path import join, dirname, isfile

# Verify if .env exists
if isfile(r"./.env"):
    # Setting .env variables
    env_path = join(dirname(__file__), r"./.env")
    load_dotenv(env_path)
    logging.info(" * Environment [Dev]")
else:
    logging.info(" * Environment [QA/PROD]")

# Spotify API Credencials
CLIENT_ID: str = str(os.environ["CLIENT_ID"])
CLIENT_SECRET: str = str(os.environ["CLIENT_SECRET"])
