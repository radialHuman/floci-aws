## install
sudo curl -fsSL https://floci.io/install.sh | sh

## check
floci doctor

## start : this will pull image of floci
sudo floci start

## set up configs
https://github.com/floci-io/floci/blob/main/docs/getting-started/aws-setup.md

## install aws-cli
pipx install awscli --upgrade --user

## Docs
https://floci.io/floci/

## Python example
import boto3

s3 = boto3.client(
    "s3",
    endpoint_url="http://localhost:4566",
    region_name="us-east-1",
    aws_access_key_id="test",
    aws_secret_access_key="test",
)
