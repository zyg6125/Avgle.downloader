import re

import requests

import AvgleErrors as Errors

HOST = 'https://avgle.com'


class Avgle():
    def __init__(self):
        self.jar = requests.cookies.RequestsCookieJar()
        self.authentication = None

    def post(self, path='/', *args, **kwargs):
        url = HOST + path
        return requests.post(url, *args, **kwargs)

    def get(self, path='/', *args, **kwargs):
        url = HOST + path
        return requests.get(url, *args, **kwargs)

    def login(self, username, password):
        payload = {
            'username': username,
            'password': password,
            'submit_login': ''
        }

        response = self.post('/login', data=payload)

        for history in response.history:
            self.jar.update(history.cookies)

        self.authentication = self.jar.get('AVS')

        return response

    def get_download(self, videoid):
        if self.authentication is None:
            print('This is a need login API')
            raise Errors.AuthAPIError

        videoid = str(videoid)
        url = '/download.php?id=' + videoid
        response = self.get(url, cookies=self.jar)

        ret = {}
        if response.history:
            ret['type'] = 'error'
        elif re.search('Torrent file not found', response.text):
            ret['type'] = 'error'
        elif re.search('magnet', response.text):
            ret['type'] = 'magnet'
            content = re.search(r'>([^<]+)</a>', response.text).group(1) + '\n'
            ret['save'] = lambda: open(videoid + '.magnet', 'w').write(content)
        elif re.search('udp://tracker', response.text):
            ret['type'] = 'torrent'
            ret['save'] = lambda: open(videoid+'.torrent','wb').write(response.content)

        return ret
