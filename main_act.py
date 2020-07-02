import requests
import requests.auth

UID = ""
SECRET = ""

def get_token(code):
    client_auth = requests.auth.HTTPBasicAuth(UID, SECRET)
    post_data = {""}