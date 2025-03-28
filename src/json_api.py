# utils/api_client.py
import requests
from ext_url_setup import BASE_URL, HEADERS


class JSONAPI:
    def get(self, endpoint, params=None):
        return requests.get(f"{BASE_URL}{endpoint}", headers=HEADERS, params=params)

    def post(self, endpoint, data=None):
        return requests.post(f"{BASE_URL}{endpoint}", headers=HEADERS, json=data)

    def put(self, endpoint, data=None):
        return requests.put(f"{BASE_URL}{endpoint}", headers=HEADERS, json=data)

    def delete(self, endpoint):
        return requests.delete(f"{BASE_URL}{endpoint}", headers=HEADERS)
