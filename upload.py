""" #!/usr/bin/env python3

import requests

response = requests.post("http://peas.pushpagiri.in:8085/ip/data_entry.php",
           data = {"ip_addre":"10.0.0.0","name":"testing","location":"Unallocated","floor":"Unallocated"})

print(response.text) """

import requests
url = "http://peas.pushpagiri.in:8085/ip/addnew_ip.php"
payload = {'ip_addre': '0005989', 'name': 'testing', 'location': 'Unallocated', 'floor': 'Unallocated'}
with requests.session() as s:
    # fetch the login page
    s.get(url)

    # post to the login form
    r = s.post(url, data=payload)
    print(r.text)


""" import requests
from requests.structures import CaseInsensitiveDict

url = "http://peas.pushpagiri.in:8085/ip/addnew_ip.php"

session = requests.Session()
headers = CaseInsensitiveDict()
headers["Content-Type"] = "application/x-www-form-urlencoded"

data = "ip_addre=10.0.0.0&name=testing&location=Unallocated&floor=Unallocated"


resp = session.post(url, headers=headers, data=data)

print(resp.status_code) """

