#!/usr/bin/env python3

import requests

response = requests.post("http://peas.pushpagiri.in:8085/ip/data_entry.php",
            files = {"ip_addre":"10.0.0.0"})

print(response.text)
