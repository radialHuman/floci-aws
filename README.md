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


## on linux
```
sudo floci start
```
```
sudo docker images
```
```
floci status
```
```
floci --help
```
```
sudo floci aws start 
```
```
sudo floci stop
```
```
floci services
```
```
sudo floci doctor
```
```
export AWS_ENDPOINT_URL=http://localhost:4566
```
```
export AWS_DEFAULT_REGION=us-east-1
```
```
export AWS_ACCESS_KEY_ID=test
```
```
export AWS_SECRET_ACCESS_KEY=test
```
```
export AWS_PROFILE=floci
```
```
export AWS_ENDPOINT_URL=http://localhost:4566
```
```
aws s3 mb s3://my-bucket --endpoint-url $AWS_ENDPOINT_URL
```


## aws cheat sheet

- [mdminhazulhaque](https://aws-cli-cheatsheet.mdminhazulhaque.io/)
- [RamuPyDev](https://github.com/RamuPyDev/MY-CLI_AWS-CheatSheet/blob/master/README.md)
- [projected1](https://gist.github.com/projected1/5be36e5c76dd27f113168773a8027f47)