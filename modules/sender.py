import requests
import json
from connector import Connector

with open('conf/urls.json') as urls: urlsData = json.load(urls)

class Sender:
    connector = None

    headers = {}
    record = {'file': '', 'hardware': "1"}


    def __init__(self):
        self.connector = Connector()

        if self.connector.active_conn() :
            self.headers = {'content-type': 'application/json', 'Authorization': 'Token ' + self.connector.get_token() }
        else:
            print('Error: Null Connector')

    def post_record(self, file, type):
        if self.connector.active_conn() :
            url = urlsData['baseApi'] + urlsData['records'] + '/'
            self.record['hardware'] = type
            self.record['file'] = file

            response = requests.post(url, data=json.dumps(self.record), headers=self.headers).json()
            print(response)

    def post_empatica_record(self, file):
        self.post_record(file, "1")

    def post_openbci_record(self, file):
        self.post_record(file, "2")

    def post_hexiwear_record(self, file):
        self.post_record(file, "3")

    def post_geotab_record(self, file):
        self.post_record(file, "4")

    def post_prediction_record(self, file):
        self.post_record(file, "5")
