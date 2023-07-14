# AWS Provisioning Scripts

Uses the AWS SDK for JavaScript to launch a set of EC2 instances.

By specifying a tag, your local /etc/host file will be updated automatically, greatly simplifying access to your instances. You no longer have to lookup the complete set of public IP addresses for the instances you just deployed, but can refer to them more simply using a predefined tag (e.g. agent1, agent2, etc.).

Prerequisites: 
- The AWS SDK for JavaScript must be installed. See [here](https://docs.aws.amazon.com/sdk-for-javascript/v2/developer-guide/installing-jssdk.html). The SDK has been added to *package.json* and can be installed by running "npm install". 
- Authenticate to AWS using *awsLogin.sh*. awsLogin requires the AWS CLI. See the script for more information


