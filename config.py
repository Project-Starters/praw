import json

config_json = json.load(open('config.json'))
"""
{
    "client_id" : "",
    "client_secret" : "",
    "user_agent" : ""
}
"""
username=config_json['username']
password=config_json['password']
client_id = config_json['client_id']
client_secret = config_json['client_secret']
user_agent = config_json['user_agent']

# reddit = praw.Reddit(client_id='my client id',
#                      client_secret='my client secret',
#                      user_agent='my user agent')