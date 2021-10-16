#!venv/bin/python
import json
import requests as requests
from dotenv import dotenv_values

config = dotenv_values('.env')
client_id = config.get('TWITCH_API_CLIENT-ID')
access_token = config.get('TWITCH_API_TOKEN')
API_HEADERS = {
    'Client-ID': client_id,
    'Authorization': f"Bearer {access_token}"
}

reqSession = requests.Session()


def checkUser(user_id):
    # send a request to twitch api and looks if the user_id is live
    url = f"https://api.twitch.tv/helix/streams?user_login={user_id}"
    is_live = False
    try:
        req = reqSession.get(url, headers=API_HEADERS)
        json_data = json.loads(req.text)['data'][0]
        if json_data['type'] == 'live':
            is_live = True
    except Exception as e:
        print(e)
        is_live = False
    return is_live
