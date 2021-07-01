import requests
import json
from connector import Connector

with open('conf/urls.json') as urls: urlsData = json.load(urls)

class Sender:
    connector = None

    headers = {}
    record = {'file': '', 'hardware': "1", 'experiment': ""}


    def __init__(self):
        self.connector = Connector()

        if self.connector.active_conn() :
            self.headers = {'content-type': 'application/json', 'Authorization': 'Token ' + self.connector.get_token() }
        else:
            print('Error: Null Connector')


    def get_last_experiment(self):
        if self.connector.active_conn() :
            url = urlsData['baseApi'] + urlsData['lastexperiments'] + '/'

            response = requests.get(url, headers=self.headers).json()
            try:
                experiment_id = int(response[0]['experiment'])

                return experiment_id
            except:
                return 0


            return experiment_id

    def create_experiment(self):
        experiment = {} #{'favorite': '', 'description': ''}

        if self.connector.active_conn() :
            url = urlsData['baseApi'] + urlsData['experiments'] + '/'
            experiment['favorite'] = False
            experiment['description'] = 'A new experiment'

            response = requests.post(url, data=json.dumps(experiment), headers=self.headers).json()
            return response

    def post_record(self, file, type):
        if self.connector.active_conn() :
            url = urlsData['baseApi'] + urlsData['records'] + '/'
            self.record['hardware'] = type
            self.record['file'] = file

            last_experiment_id = self.get_last_experiment()
            if last_experiment_id:
                self.record['experiment'] = str(last_experiment_id)
            else:
                newExperimentID = self.create_experiment()['experimentData']['id']
                self.record['experiment'] = str(newExperimentID)
            #print(str(self.record['experiment']))
            #print(json.dumps(self.record))
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
