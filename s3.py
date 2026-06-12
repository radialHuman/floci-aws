import boto3

def main():
    s3 = boto3.client(
        "s3",
        endpoint_url="http://localhost:4566",
        region_name="us-east-1",
        aws_access_key_id="test",
        aws_secret_access_key="test",
    )

    print(s3)

if __name__ == "__main__":
    main()