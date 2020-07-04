import requests, json

UID = ""
SECRET = ""

def get_token(code):
    client_auth = requests.auth.HTTPBasicAuth(UID, SECRET)
    post_data = {""}

oauth_data = {
    'grant_type': 'client_credentials',
    'client_id': UID,
    'client_secret': SECRET,
}
oauth_url = "https://api.intra.42.fr/oauth/token"
api_url = "https://api.intra.42.fr/v2/"

oauth_request = requests.post(oauth_url, data=oauth_data)
