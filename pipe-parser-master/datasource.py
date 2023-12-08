import boto3

s3 = boto3.resource('s3')


def read_file(bucket, key):
    obj = s3.Object(bucket, key)
    return obj.get()['Body'].read().decode('utf-8')
