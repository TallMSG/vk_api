from urllib.parse import urlencode

APP_ID = 7056606
AUTH_URL = 'https://oauth.vk.com/authorize'
AUTH_DATA = {
    'client_id': APP_ID,
    'display': 'page',
    'scope': 'friends',
    'response_type': 'token'
}

# print('?'.join((AUTH_URL, urlencode(AUTH_DATA))))


