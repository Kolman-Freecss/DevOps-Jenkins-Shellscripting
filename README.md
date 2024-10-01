# DevOps with focus Jenkins 

This project is a repository to show the DevOps process with top tech stack.

- Jenkins set up with docker-compose
- Automatization Jenkins jobs with Python.
- Integration Jenkins with AWS
- Terraform to create infrastructure on AWS with a Jenkins implementation.

# Index

- [Getting Started](#getting-started)
  - [AWS Configuration](#aws-configuration)
    - [Trigger Terraform pipeline](#trigger-terraform-pipeline)
    - [Connect to EC2 instance](#connect-to-ec2-instance)
- [Dependencies](#dependencies)
- [Tech stacks CI/CD](#tech-stacks-ci/cd)

# Getting Started

## Local installation

Config Jenkins on your local machine:

1. Execute `docker-compsoe.yml` from `.docker/local` folder.
2. Go to `localhost:8080` and follow the instructions to configure Jenkins. (Create an initialAdminPassword)
3. Install Git plugin for Jenkins. (This is necessary to trigger pipelines with SCM option enabled)

## AWS Configuration

Implantation of Jenkins automated with Terraform on AWS. 

Requirements:
- Create your AWS account.
- Create your Access Key in the Security Credentials section.
- Take an AMI valid for your region.
- Configure SSH key pair in your AWS account for EC2 instances.
- Configure VPC.
- Configure Subnet.

1. Configure AWS CLI with your credentials:

```bash
aws configure

# AWS Access Key ID [None]: YOUR_ACCESS_KEY
# AWS Secret Access Key [None]: YOUR_SECRET_ACCESS_KEY
```

2. Go to AMI Catalog and take an AMI ID for your region.

Put your AMI ID in `main.tf` file.

3. Configure your SSH key pair in `main.tf` file.

```bash
aws ec2 create-key-pair --key-name my-ssh-key --query 'KeyMaterial' --output text > my-ssh-key.pem
```


### Trigger Terraform pipeline

Project has different .tf files decoupled by behaviour. Terraform will treat all files as an unique project.

1. Init Terraform: 

```bash
terraform init
```

2. Plan Terraform:

```bash
terraform plan
```

3. Apply Terraform:

```bash
terraform apply
```

4. Destroy Terraform:

```bash
terraform destroy
```

### Connect to EC2 instance

Here we've different ways to connect to EC2 instance:

1. Using SSH command:

```bash
# Create your SSH key pair previously in the EC2 AWS section.
ssh -i my-ssh-key.pem ec2-user@YOUR_EC2_PUBLIC_IP
```

# Dependencies

- Jenkins API

# Tech stacks CI/CD

- Jenkins
- Docker & Docker Compose
- AWS

# Troubleshoting

- Script to install Jenkins not working properly. 
  - Alternative Solution: Connect through SSH to the EC2 instance and install Jenkins manually. (https://mirrors.jenkins.io/redhat-stable/)
    - After that connect to the IPv4 Public EC2 instance with HTTP protocol and port 8080.
      - Example: http://YOUR_EC2_PUBLIC_IP:8080
- Check SSH key permissions to connect to EC2 instance.
  - `chmod 400 my-ssh-key.pem`
  - Remove permissions to other group users or another users because AWS won't let you connect to the EC2 instance if the permissions are too permissive.
- Check EC2 system log from AWS section to see if Jenkins is running properly or installed.
- https://community.jenkins.io/t/issue-while-upgrading-plugins-on-latest-jenkins/9846
- It takes its time to start even if the instance is running. Be patient. :)
  - Check logs with
    - ```bash
      aws ec2 get-console-output --instance-id YOUR_INSTANCE_ID --output text
      ```

---

Shield: [![CC-BY-NC-ND 4.0][CC-BY-NC-ND-shield]][CC-BY-NC-ND]

This work is licensed under a [Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International License.][CC-BY-NC-ND]

[![CC-BY-NC-ND 4.0][CC-BY-NC-ND-image]][CC-BY-NC-ND]

[CC-BY-NC-ND-shield]: https://img.shields.io/badge/License-CC--BY--NC--ND--4.0-lightgrey
[CC-BY-NC-ND]: http://creativecommons.org/licenses/by-nc-nd/4.0/
[CC-BY-NC-ND-image]: https://i.creativecommons.org/l/by-nc-nd/4.0/88x31.png
