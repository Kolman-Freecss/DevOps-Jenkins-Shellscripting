import jenkins

jenkins_url = 'http://localhost:8080'
username = 'kolman'
api_token = '1234' # Get it from Jenkins > User > Configure
jenkins_service = jenkins.Jenkins(jenkins_url, username, api_token)

# Jenkins version
user = jenkins_service.get_whoami()
version = jenkins_service.get_version()
print('Hello %s from Jenkins %s' % (user['fullName'], version))

job_name = 'jenkins_trigger_python'
# --------- Job Configuration ---------
job_config = open('data/03_jenkins_trigger_python.xml').read()

try:
    # --------- Create a new job ---------
    print(f'Creating job {job_name}')
    if jenkins_service.job_exists(job_name):
        jenkins_service.delete_job(job_name)
    jenkins_service.create_job(job_name, job_config)

    # --------- Build a job ---------
    print(f'Building job {job_name}')
    jenkins_service.build_job(job_name)
except Exception as e:
    print("Error: ", e)
    exit(1)