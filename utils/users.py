""" Helper functions for working with github users """

import requests
import config


# helper to get a user from GitHub
def get_user(username):
    response = requests.get(f'{config.GITHUB_API_URL}users/{username}')

    if response.status_code:
        return response.json()
    
    else:
        return None