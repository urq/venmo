'''
Transfer module.
'''
import sys

import requests

import venmo


def transfer(amount):
    access_token = venmo.auth.get_access_token()
    bank_account_id = venmo.auth.get_bank_account_id()
    response = requests.post(
        venmo.settings.CASHOUTS_URL,
        params={'access_token': access_token},
        data={'amount': amount, 'bank_account_id': bank_account_id}
    ).json()
    if 'error' in response:
        print(response['error']['message'])
        sys.exit(1)
    else:
        print('Transferring {} to {} on {}.\nNew balance: {}'.format(
            amount,
            response['bank_name'],
            response['next_business_day'],
            str(response['balance'])))
