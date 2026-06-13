
## create a s3 bucket
```
aws s3 mb s3://my-bucket --endpoint-url $AWS_ENDPOINT_URL
```

## list all s3 buckets created
```
aws s3 ls
```

## create a sqs queue
```
aws sqs create-queue --queue-name queue-test-1  --endpoint-url $AWS_ENDPOINT_URL
```