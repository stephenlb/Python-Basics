import requests
from functools import partial

def farlessthanafew(a,b):
    return a * b

mult100 = partial(farlessthanafew, b=100)
print(f'{mult100(10)}')

## Wrap the GET method in requests lib
user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36'
headers = { 'User-Agent': user_agent }
chromeFetch = partial(requests.get, headers=headers)

response = chromeFetch('https://www.google.com/')

print(response.text)
