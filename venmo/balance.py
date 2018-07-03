
'''
Balance module.
'''
import sys

import requests

import venmo


def balance():
    access_token = venmo.auth.get_access_token()
    response = requests.get(
        venmo.settings.BALANCE_URL,
        params={'access_token': access_token}
    )
    res = response.json()
    if 'error' in res:
        print(res['error']['message'])
        sys.exit(1)
    else:
        print('{balance:.2f}'.format(balance=res['balance']))
