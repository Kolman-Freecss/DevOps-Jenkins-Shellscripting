import json
import os

import jenkins
import requests

jenkins_url = os.getenv('JENKINS_URL')
username = os.getenv('JENKINS_USER')
api_token = os.getenv('JENKINS_API_TOKEN')   # Get it from Jenkins > User > Configure
jenkins_service = jenkins.Jenkins(jenkins_url, username, api_token)

# Jenkins version
user = jenkins_service.get_whoami()
version = jenkins_service.get_version()
print('Hello %s from Jenkins %s' % (user['fullName'], version))

# Github settings
github_token = os.getenv('ACCESS_TOKEN')
repo_name = 'Kolman-Freecss/DevOps-Jenkins-Shellscripting-AWS-Python'
github_api_url = f'https://api.github.com/repos/{repo_name}/hooks'

job_config = open('.data/main_build_webhook.xml').read()

try:
    jenkins_service.create_job('main-build-webhook', job_config)
    print('Job created successfully')
except Exception as e:
    print('Job already exists or something went wrong')

# Webhook data
webhook_data = {
    "name": "web",
    "active": True,
    "events": ["push"],
    "config": {
        "url": f"{jenkins_url}/github-webhook/",
        "content_type": "json"
    }
}

# Headers for Github API
headers = {
    "Authorization": f"token {github_token}",
    "Accept": "application/vnd.github.v3+json"
}

response = requests.post(github_api_url, data=json.dumps(webhook_data), headers=headers)

if response.status_code == 201:
    print('Webhook created successfully')
else:
    print(f'Error: {response.status_code} {response.text}')



