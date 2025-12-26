#!/usr/bin/env python

"""
WIFIHacker - Wireless Penetration Testing Tool
----------------------------------------------
"""


def paths():

    redirect_paths = [
                "/", "/index.html",
                "/generate_204", "/gen_204",
                "/mobile/status.php",                          # Samsung-specific
                "/hotspot-detect.html",                        # Apple
                "/ncsi.txt", "/connecttest.txt", "/redirect",  # Windows & others
                "/success.txt", "/favicon.ico",
                "/connectivity-check.html"
            ]
    return redirect_paths


def credfile():
    CRED_FILE = "/../../includes/config/credentials.json"
    return CRED_FILE

def port():
    PORT = 80
    return PORT