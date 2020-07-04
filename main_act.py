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

def count_page(num) :
    if (num) <= 100:
        return 1
    page : int = int(num / 100) + 1 if num % 100 != 0 else int(num / 100)
    return page

def get_data(url, page, per_page, sort) :
    params = {
    'access_token' : access_token,
    'page' : page if page else '',
    'per_page' : per_page if per_page else '',
    'sort' : sort if sort else '',
    }
    return requests.get(f'{api_url}{url}', params=params).json()
count = 0
#print(requests.get(f'{api_url}users/68929', params={'access_token':access_token}).json())
number = requests.get(f'{api_url}campus/29', params={'access_token' : access_token}).json()["users_count"]
page = count_page(number)
crawlings = [get_data(url="cursus/21/users?filter[primary_campus_id]=29",page=x, per_page=100, sort = "login")
            for x in range (1, int(page) + 1)]
for crawling in crawlings :
    for user in crawling :
        user_id = user['id']
        user_login = user['login']
        cursus = requests.get(f'{api_url}users/{user_id}', params = {'access_token' : access_token}).json()#["cursus_users"]
        if cursus.get("cursus_users") :
            cursus_user = cursus["cursus_users"]
            if len(cursus_user) < 2 :
                continue
            level = cursus_user[1]["level"]
            if 2.50 <= level <= 3.0 :
                print(user_login)
                count += 1
                print(count)


#    idx += 1
#    print (idx)
    #level = cursus_user.json()["level"]
    #print(level)
    #level = requests.get(f'{api_url}/users/crawling')    
#21
#number = requests.get(f'{api_url}cursus/29', params={'access_token' : access_token}).json()["users_count"]
#page = count_page(number)
#crawlings = [get_data(url="cursus/", page=x, per_page=100, sort = "login")
#            for x in range (1, int(page) + 1)]
#for crawling in crawlings:
#    for data in crawling:
#        print(data["cursus"])








#for i in users_in_cursus :
#    if i.json()["login"] == "ryukim"
# requests.get(f'{api_url}campus/29/users', params=params).json()
#print(users_in_cursus)
#29 

