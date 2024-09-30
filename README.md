# DevOps with focus Jenkins 

This project is a repository to show the DevOps process with top tech stack.

- Jenkins set up with docker-compose
- Automatization Jenkins jobs with Python.
- Integration Jenkins with AWS
- Terraform to create infrastructure on AWS with Jenkins

## Index

- [Getting Started](#getting-started)
- [Dependencies](#dependencies)
- [Tech stacks CI/CD](#tech-stacks-ci/cd)

## Getting Started

Config Jenkins on your local machine:

1. Execute `docker-compsoe.yml` from `.docker/local` folder.
2. Go to `localhost:8080` and follow the instructions to configure Jenkins. (Create an initialAdminPassword)
3. Install Git plugin for Jenkins. (This is necessary to trigger pipelines with SCM option enabled)

### AWS Configuration

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

## Dependencies

- Jenkins API

## Tech stacks CI/CD

- Jenkins
- Docker & Docker Compose
- AWS

## Troubleshoting


---

Shield: [![CC-BY-NC-ND 4.0][CC-BY-NC-ND-shield]][CC-BY-NC-ND]

This work is licensed under a [Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International License.][CC-BY-NC-ND]

[![CC-BY-NC-ND 4.0][CC-BY-NC-ND-image]][CC-BY-NC-ND]

[CC-BY-NC-ND-shield]: https://img.shields.io/badge/License-CC--BY--NC--ND--4.0-lightgrey
[CC-BY-NC-ND]: http://creativecommons.org/licenses/by-nc-nd/4.0/
[CC-BY-NC-ND-image]: https://i.creativecommons.org/l/by-nc-nd/4.0/88x31.png
