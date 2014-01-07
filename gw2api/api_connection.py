__author__ = 'Wayne'
import json
import requests

base_url = 'https://api.guildwars2.com/v1/'
suffix = '.json'
headers = {
    'Accept': 'application/json',
    'User-Agent': 'GW2CT'
}


def api_request(uri):
    url = base_url + uri + suffix

    print('GW2API making a request to: %s' % url)
    r = json.loads(requests.get(url, params=None, headers=headers).text)

    return r
