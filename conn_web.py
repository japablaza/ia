#!/usr/bin/python

import requests
import os

user_endpoint = os.environ.get("joomla_user")
passwd_endpoint = os.environ.get("joomla_api")
base_url = "https://beta.futuropresente.org"
users_endpoint = "/api/index.php/v1/users"

print(passwd_endpoint)