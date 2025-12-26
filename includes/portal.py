#!/usr/bin/env python

"""
WIFIHacker - Wireless Penetration Testing Tool
----------------------------------------------

"""


import json
import os

CRED_FILE = "includes/config/credentials.json"

def get_credentials_json():
    if not os.path.exists(CRED_FILE):
        return []
    with open(CRED_FILE, "r") as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            return []
