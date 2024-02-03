"""About API"""

import requests

response = requests.get('http://api.open-notify.org/iss-now.json')
response.raise_for_status()
print(response)
print(response.status_code)


x = response.json()
print(x)
for key in x:
    print(x[key])


