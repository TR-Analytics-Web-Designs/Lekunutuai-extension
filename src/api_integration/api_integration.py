import requests

# Define API endpoints and keys
linkedin_api_url = 'https://api.linkedin.com/v2/me'
facebook_api_url = 'https://graph.facebook.com/me'
twitter_api_url = 'https://api.twitter.com/2/tweets'

linkedin_access_token = 'your_linkedin_access_token'
facebook_access_token = 'your_facebook_access_token'
twitter_bearer_token = 'your_twitter_bearer_token'

# Function to get LinkedIn profile
def get_linkedin_profile():
    headers = {'Authorization': f'Bearer {linkedin_access_token}'}
    response = requests.get(linkedin_api_url, headers=headers)
    return response.json()

# Function to get Facebook profile
def get_facebook_profile():
    response = requests.get(f'{facebook_api_url}?access_token={facebook_access_token}')
    return response.json()

# Function to get Twitter tweets
def get_twitter_tweets():
    headers = {'Authorization': f'Bearer {twitter_bearer_token}'}
    response = requests.get(twitter_api_url, headers=headers)
    return response.json()

linkedin_profile = get_linkedin_profile()
facebook_profile = get_facebook_profile()
twitter_tweets = get_twitter_tweets()

print('LinkedIn Profile:', linkedin_profile)
print('Facebook Profile:', facebook_profile)
print('Twitter Tweets:', twitter_tweets)

# /api_integration/api_integration.py

import requests

class APIIntegration:
    def __init__(self, base_url):
        self.base_url = base_url

    def get_data(self, endpoint):
        response = requests.get(f"{self.base_url}/{endpoint}")
        return response.json()

    def post_data(self, endpoint, data):
        response = requests.post(f"{self.base_url}/{endpoint}", json=data)
        return response.json()

# Usage
api = APIIntegration("https://api.example.com")
link_data = api.get_data("links")
transaction_data = api.get_data("transactions")
