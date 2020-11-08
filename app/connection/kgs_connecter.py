import json, requests

LOGIN_DATA = {
    "type": "LOGIN",
    "name": "truongcam",
    "password": "123456",
    "locale": "en_US"
}

KGS_API = 'https://www.gokgs.com/json/access'

def getUserInfo(name):
    req_data = {
        'type': 'JOIN_ARCHIVE_REQUEST',
        'name': name
    }
    req_login = requests.post(url = KGS_API, json = LOGIN_DATA)
    cookies = req_login.cookies
    if req_login.status_code == 200:
        req_info = requests.post(url = KGS_API, json = req_data, cookies = cookies)
        if req_info.status_code == 200:
            req_get = requests.get(url = KGS_API, cookies = cookies)
            infos = req_get.json()
            for info in infos['messages']:
                if 'type' in info and info['type'] == 'ARCHIVE_JOIN':
                    return info
    return None