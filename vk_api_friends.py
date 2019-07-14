import requests

TOKEN = 'a2bad16bd44d9f5eabb06da33c18872150bff5333be72592b55a2d9e6e69cecd448a2a1f36552bbd30a4c'

class User:

    def __init__(self, token):
        self.token = token

    def get_params(self):
        user1_id = input('Введите id первого пользователя: ')
        user2_id = input('Введите id второго пользователя: ')
        return {
            'access_token': self.token,
            'v':'5.52',
            'source_uid': user1_id,
            'target_uid': user2_id
        }

    def mutual_friends(self):
        params = self.get_params()
        response = requests.get(
            'https://api.vk.com/method/friends.getMutual',
            params=params
        )
        return response.json()['response']


Sergey = User(TOKEN)
mutual_friends = Sergey.mutual_friends()
print('Общие друзья первого и второго пользователя:')
for el in mutual_friends:
    print(f'https://vk.com/id{el}')
