import requests
import json
import base64


class PicnicAuthClient(object):
    def __init__(self, base_endpoint, api_key):
        self.base_endpoint = base_endpoint
        self.api_key = api_key
        self.authorization_header = {
            'Authorization': 'Bearer {}'.format(api_key)
        }

    def create_request_url(self, endpoint_url):
        return self.base_endpoint + endpoint_url

    def login(self, username, password):
        request_url = self.create_request_url('tokens')
        request = requests.post(request_url, headers=self.authorization_header,
                                data={'username': username, 'password': password})

        return request

    def get_auth_users(self, page=1, page_count=10):
        request_url = self.create_request_url('Companies/Me/AuthUsers')
        request = requests.get(request_url, headers=self.authorization_header,
                               params={'page': page, 'pageCount': page_count})

        return request

    def add_auth_user(self, external_id, username, email):
        request_url = self.create_request_url('AuthUsers')
        request = requests.post(request_url, headers=self.authorization_header,
                                data={'ExternalId': external_id, 'UserName': username, 'Email': email})

        return request

    
