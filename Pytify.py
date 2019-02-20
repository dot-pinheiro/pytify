import requests
import base64

class Pytify:

    def __init__(self, client_id, client_secret, redirect_uri):
        self.__client_id = client_id
        self.__client_secret = client_secret
        self.__redirect_uri = redirect_uri
        self.__default_endpoint = 'https://api.spotify.com/v1'

    def auth(self, code):
        auth_url = 'https://accounts.spotify.com/api/token'
        data = {
            'grant_type': 'authorization_code',
            'code': code,
            'redirect_uri': self.__redirect_uri,
        }
        encoded_header = self.__client_id+':'+self.__client_secret
        encoded_header = 'Basic ' + base64.b64encode(encoded_header.encode('utf-8')).decode('utf-8')
        headers = {
            'Authorization': encoded_header
        }
        response = requests.post(url=auth_url, data=data, headers=headers)
        return response

    def get_current_user_profile(self, access_token):
        endpoint = self.__default_endpoint + '/me'
        headers = {
            'Authorization': 'Bearer ' + access_token,
            'Content-Type': 'application/json'
        }
        response = requests.get(url=endpoint, data={}, headers=headers)
        return response.json()

    def get_recently_tracks(self, access_token):
        endpoint = self.__default_endpoint + '/me/player/recently-played'
        headers = {
            'Authorization': 'Bearer ' + access_token,
            'Content-Type': ' application/json'
        }
        response = requests.get(url=endpoint, data={}, headers=headers)
        return response.json()
