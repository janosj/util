#!/usr/local/bin/python3

# Pulls cached SSO credentials and exports them to credentials file.
# Required for aws-sdk scripts that are not yet SSO-aware.

import boto3
import os
 
session = boto3.Session()
creds = session.get_credentials()

homedir = os.environ.get('HOME')
f = open(homedir + "/.aws/credentials", "w")

f.write("[default]\n")
f.write("aws_access_key_id = " + creds.access_key + "\n")
f.write("aws_secret_access_key = " + creds.secret_key + "\n")
f.write("aws_session_token = " + creds.token + "\n")

f.close()
 
