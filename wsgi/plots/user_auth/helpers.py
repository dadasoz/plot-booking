import requests
from django.conf import settings

class LoginHelper(object):

    def generate_oauth_token(self, request, username, password):
        client_id = settings.CLIENT_ID
        client_secret = settings.CLIENT_SECRET

        headers = {'Content-Type': 'application/x-www-form-urlencoded'}
        payload = {'grant_type': 'password',
                   'username': username,
                   'password': password,
                   'client_id': client_id,
                   'client_secret': client_secret}

        host = request.get_host()
        return (requests.post(
                settings.SERVER_PROTOCOLS + host + "/o/token/",
                data=payload,
                headers=headers))
