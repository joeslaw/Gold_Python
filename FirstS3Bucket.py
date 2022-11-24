import bota3

aws_resource=bota3.resource("s3")
bucket=aws_resource.Bucket("myfirstbucketslaw2358923")
response = bucket.create(
    ACL='public-read',
    CreateBucketConfiguration={
        'LocationConstraint': 'us-east-2'
    },
)
print(response)