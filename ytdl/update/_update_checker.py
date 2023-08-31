import requests
from ..version import __version__
from .updater import *


def check_for_update(url: str):
    response = requests.get(url)
    data = response.json()
    latest_tag = data["tag_name"]
    print(latest_tag)
    if latest_tag > __version__:
        print("update")