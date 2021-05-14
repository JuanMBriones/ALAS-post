import requests
import json

with open('conf/credentials.json') as credentials: userData = json.load(credentials)
with open('conf/urls.json') as urls: urlsData = json.load(urls)

class Connector:
    token = str("")

    headers = {'content-type': 'application/json'}

    def authenticate(self):
        urlAuth = urlsData['base'] + urlsData['auth'] + '/'
        response = requests.post(urlAuth, data=json.dumps(userData), headers=self.headers).json()

        try:
            self.token = response['token']
        except:
            print('ERROR 400: Authentication error')

    def active_conn(self):
        return self.token != ""

    def get_token(self):
        if self.active_conn():
            return self.token

    def __init__(self):
        self.authenticate()
