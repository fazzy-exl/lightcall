import json
import os

CONFIG_FILE = "config.json"


def load_settings():

    if not os.path.exists(CONFIG_FILE):
        return {"username": ""}

    with open(CONFIG_FILE, "r") as f:
        return json.load(f)


def save_settings(data):

    with open(CONFIG_FILE, "w") as f:
        json.dump(data, f)