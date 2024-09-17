import time

import jenkins
import requests
from requests.auth import HTTPBasicAuth

jenkins_url = 'http://localhost:8080'
username = 'kolman'
api_token = '1234' # Get it from Jenkins > User > Configure
jenkins_service = jenkins.Jenkins(jenkins_url, username, api_token)

# Jenkins version
user = jenkins_service.get_whoami()
version = jenkins_service.get_version()
print('Hello %s from Jenkins %s' % (user['fullName'], version))

# --------- Delete a job if exists ---------
if jenkins_service.job_exists('my-new-job'):
    jenkins_service.delete_job('my-new-job')
if jenkins_service.job_exists('api-test'):
    jenkins_service.delete_job('api-test')

# --------- Create a new job ---------
# Get 01_create_job.xml file content
job_config = open('.data/01_create_job.xml').read()

# Method 1
# response = requests.post(
#     f'{jenkins_url}/createItem?name=my-new-job',
#     auth=HTTPBasicAuth(username, api_token),
#     headers={'Content-Type': 'application/xml'},
#     data=job_config
# )
# print(response.status_code, response.text)

# Method 2
jenkins_service.create_job('my-new-job', job_config)

# --------- Get a job ---------
job = jenkins_service.get_job_config('my-new-job')
print(job)

# --------- Build a job ---------
jenkins_service.build_job('my-new-job')

# --------- Disable a job ---------
jenkins_service.disable_job('my-new-job')

# --------- Copy a job ---------
jenkins_service.copy_job('my-new-job', 'api-test')

# --------- Enable a job ---------
jenkins_service.enable_job('api-test')

# --------- Reconfig a job ---------
# Get 02_reconfig_job.xml file content
job_config = open('.data/02_reconfig_job.xml').read()
jenkins_service.reconfig_job('api-test', job_config)

# build a parameterized job
# requires creating and configuring the api-test job to accept 'param1' & 'param2'
try:
    jenkins_service.build_job('api-test', {'param1': 'test value 1', 'param2': 'test value 2'})
    # Wait for the build to finish
    print('Waiting for the build to finish...')
    time.sleep(5)
    # Get the last build
    last_build_number = jenkins_service.get_job_info('api-test')['lastCompletedBuild']['number']
    build_info = jenkins_service.get_build_info('api-test', last_build_number)
    print(build_info)
except Exception as e:
    print("Error: ", e)

# --------- Get all jobs ---------
jobs = jenkins_service.get_jobs()

print("Getting all jobs")
for job in jobs:
    print(job['name'])



# --------- Get all views ---------
views = jenkins_service.get_views()

print("Getting all views")
for view in views:
    print(view['name'])

# --------- Delete a view if exists ---------
if jenkins_service.view_exists('my-new-view'):
    jenkins_service.delete_view('my-new-view')

# --------- Create a new view (empty) ---------
jenkins_service.create_view('my-new-view', jenkins.EMPTY_VIEW_CONFIG_XML)
view_config = jenkins_service.get_view_config('my-new-view')
print(view_config)

# --------- Jenkins plugins ---------
# Get all plugins
try:
    print("Getting plugins")
    plugins = jenkins_service.get_plugins()
    for plugin in plugins:
        print(plugin['shortName'], plugin['version'])
except Exception as e:
    print("Error: ", e)

# --------- Jenkins nodes ---------
# Get all nodes
try:
    nodes = jenkins_service.get_nodes()
    for node in nodes:
        print(node['displayName'])
except Exception as e:
    print("Error: ", e)

try:
    # Remove a node if exists
    if jenkins_service.node_exists('my-new-node'):
        jenkins_service.delete_node('my-new-node')

    # Create a new node
    jenkins_service.create_node('my-new-node', '1', 'Test node')
    nodes = jenkins_service.get_nodes()
    print("Created node: ")
    print(nodes)

    node_config = jenkins_service.get_node_config('my-new-node')
    print("Node config: ")
    print(node_config)

    # Disable a node
    print("Disabling node")
    jenkins_service.disable_node('my-new-node')

    # Enable a node
    print("Enabling node")
    jenkins_service.enable_node('my-new-node')
except Exception as e:
    print("Error: ", e)

# Create node with parameters
try:
    params = {
        'port': '22',
        'username': 'kolman',
        'credentialsId': '1234',
        'host': 'my.jenkins.slave1'
    }
    print("Creating node with parameters")
    jenkins_service.create_node(
        'my-new-node',
        nodeDescription='my test slave',
        remoteFS='/home/juser',
        labels='precise',
        exclusive=True,
        launcher=jenkins.LAUNCHER_SSH,
        launcher_params=params)
except Exception as e:
    print("Error: ", e)


