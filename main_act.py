import requests
import json

UID = ""
SECRET = ""

oauth_data = {
    'grant_type' : 'client_credentials',
    'client_id' : UID,
    'client_secret' : SECRET,
}
oauth_url = "https://api.intra.42.fr/oauth/token"
api_url = "https://api.intra.42.fr/v2/"

oauth_request = requests.post(oauth_url, data = oauth_data)
print(oauth_request.json())
access_token = oauth_request.json()['access_token']
print(requests.get(f'{api_url}cursus', params={'access_token' : access_token}).json())
#29