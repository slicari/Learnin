import requests
import lxml

login_url = 'https://member.expireddomains.net/login/'
req_url = 'https://member.expireddomains.net/domains/combinedexpired/'

# name = "login"
# name = "password"

# Replace these with a variable and store credentials in a separate file
payload = {
    'login': 'slicari',
    'password': ';H_bN=a^N8=4w_Sb'
}

with requests.Session() as session:
    post = session.post(login_url, data = payload)
    r = session.get(req_url)
    print(r.text)