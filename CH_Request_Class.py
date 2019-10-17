# This is on hold as the company house API is a bit naff

import requests
import json
from local_config import api_key


def jprint(obj):
    txt = json.dumps(obj, sort_keys=True, indent=4)
    return txt


response = requests.get("http://api.open-notify.org/iss-pass.json", params=latlong)

print(response.status_code)
js = jprint(response.json())


class CompnayHouse:

    def __init__(self, key, start_year, end_year):
        self.key = key
        self.start_year = start_year
        self.end_year = end_year

    def get(self):
        payload = {"api_key" : api_key}
        response = requests.get()
        return response
