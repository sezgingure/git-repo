# ДЗ 1

import requests
from pprint import pprint

headers = {'User Agent':'Chrome/76.0.3809.100'}
link = 'https://api.github.com/users/sezgingure/repos'
req = requests.get(link)

pprint(req.json())
req.close()

# ДЗ 2

# буду делать