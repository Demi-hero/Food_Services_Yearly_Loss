import requests
import json
from local_config import api_key


def jprint(obj):
    txt = json.dumps(obj, sort_keys=True, indent=4)
    return txt


latlong = {
    "lat": 51.478645,
    "lon": -0.156657
}
response = requests.get("http://api.open-notify.org/iss-pass.json", params=latlong)

print(response.status_code)
json = jprint(response.json())


class CompnayHouse:

    def __init__(self, key):
        self.key = key
