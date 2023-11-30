import os
import json
from .connecting import obj


def load_tokens_auth():

    if not os.path.exists('config/tokens.json'):
        with open('config/tokens.json', 'w') as file:
            json.dump({}, file)

    with open('config/tokens.json', 'r') as file:
        data = json.load(file)

    if data != {}:
        obj.xsrf = data['xsrf']
        obj.hhtoken = data['hhtoken']
