#!/usr/bin/python

import requests
import os
import json
import pprint

# user_endpoint = os.environ.get("joomla_user")
passwd_endpoint = os.environ.get("joomla_api")
base_url = "https://beta.futuropresente.org"
base_path = "/api/index.php/v1"
# end_point = "/users"
end_point = "/content/articles/146"

url = base_url + end_point


url = base_url + base_path + end_point

payload = {}
headers = {
  'X-Joomla-Token': passwd_endpoint
}

response = requests.request("GET", url, headers=headers, data=payload)

pp = pprint.PrettyPrinter(indent=4)

pp.pprint(response.text)

pprint.pprint(response.text)

def post_article(title, alias, articletext, catid):

    url = "https://beta.futuropresente.org/api/index.php/v1/content/articles"

    payload = json.dumps({
      "alias": alias,
      "articletext": articletext,
      "catid": catid,
      "language": "*",
      "metadesc": "",
      "metakey": "",
      "title": title
    })
    headers = {
      'Content-Type': 'application/json',
      'X-Joomla-Token': passwd_endpoint
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    print(response.text)
