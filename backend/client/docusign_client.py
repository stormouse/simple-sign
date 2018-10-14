config = {
    'user_id' : '47d18417-21e7-4725-98d8-0091192322c9',
    'template_id' : '53d55092-6cd6-4b8b-8d02-449e4420ca96',
    'access_token' : 'eyJ0eXAiOiJNVCIsImFsZyI6IlJTMjU2Iiwia2lkIjoiNjgxODVmZjEtNGU1MS00Y2U5LWFmMWMtNjg5ODEyMjAzMzE3In0.AQgAAAABAAUABwAAquyFIzHWSAgAAOoPlGYx1kgCABeE0UfnISVHmNgAkRkjIskVAAEAAAAYAAEAAAAFAAAADQAkAAAAZjBmMjdmMGUtODU3ZC00YTcxLWE0ZGEtMzJjZWNhZTNhOTc4MAAAmP1rIDHWSA.AH4lyaaT0Ywa-QoEO3PgLt1rCS8ucAswdvJUthl8eEEBKR4Pn5QHpxNks156aMqmAeM97cwcIBR4M-RMN2DjMehKM6Y8PotA31-wobdznT5uSmiS-ijX9CU-xNhhRrNluQidYzu_o8zu65XLGykJnXD-3ln5cvsMqTm0eUnXo0rkUBKOXEz-UH6-NH81oTwgIUqdvvMQ6MO2Lsc7_LgQEg0j773e9VzmN3uciskJkmW6P9Zciei9ZJkyAxgXinDJ5du_doOB9Em3wEzethZ2LYgKZ2OW3Utc8YDWyvKoCyiG_MA-Em8GkQFk1ZKeKRt2G8Orhpoc0xnhnzP4gma0Ag',
    'integrator_key' : '1f5eef3b-7e41-4282-b720-b44717fffc18',
    'secret_key' : '6a8e7ee7-b839-41f1-9eaf-1afbd2015f61',
    'account_id' : 'e28aad58-0465-4f43-90f0-7f87b5db6660',
}



import requests
import json
import copy


class DocuSignDemoClient(object):

    def __init__(self, access_token, integrator_key, developer_info):
        self.base_url = "https://demo.docusign.net/restapi"
        self.access_token = access_token
        self.integrator_key = integrator_key
        self.default_header = {
            "Content-Type" : "application/json; charset=utf-8",
            "Authorization" : "Bearer " + access_token,
        }
        self.userinfo = self.get_user_info()
        self.account_id = self.userinfo['accounts'][0]['account_id']
        self.user_id = self.userinfo['sub']
        self.user_name = self.userinfo['name']
        self.user_email = self.userinfo['email']
        self.developer_info = developer_info
        self.xauth_header = {
            'X-DocuSign-Authentication': json.dumps({
                'Username': self.developer_info['username'],
                'Password': self.developer_info['password'],
                'IntegratorKey': self.integrator_key,
            })
        }

    def get_user_info(self):
        r = requests.get('https://account-d.docusign.com/oauth/userinfo', headers=self.default_header)
        return r.json()


    def list_envelopes(self):
        target_url = self.base_url + '/v2/accounts/' + self.account_id + '/envelopes'
        query = {'from_date': '2010-01-01'}
        r = requests.get(target_url, params=query, headers=self.default_header)
        return r.json()


    def create_envelope(self, envelope_data):
        target_url = self.base_url + "/v2/accounts/" + self.account_id + "/envelopes"
        headers = copy.deepcopy(self.xauth_header)
        headers.update(self.default_header)
        r = requests.post(target_url, json=envelope_data, headers=headers)
        return r.json()


    def list_templates(self):
        target_url = self.base_url + '/v2/accounts/' + self.account_id + '/templates'
        r = requests.get(target_url, headers=self.default_header)
        return r.json()

    
    def create_template(self, template_data):
        target_url = self.base_url + '/v2/accounts/' + self.account_id + '/templates'
        headers = copy.deepcopy(self.xauth_header)
        headers.update(self.default_header)
        r = requests.post(target_url, json=template_data, headers=headers)


    def update_template(self, template_id, updated_data):
        target_url = self.base_url + '/v2/accounts/' + self.account_id + '/templates/' + template_id
        headers = copy.deepcopy(self.xauth_header)
        headers.update(self.default_header)
        r = requests.put(target_url, json=updated_data, headers=headers)
        return r.json()


    def get_template(self, template_id):
        target_url = self.base_url + '/v2/accounts/' + self.account_id + '/templates/' + template_id
        print(target_url)
        r = requests.get(target_url, headers=self.default_header)
        return r.json()


ds_client = DocuSignDemoClient(config['access_token'], config['integrator_key'], {'username':'stormouse@gmail.com', 'password':'--------'})
