#Reference - https://realpython.com/lessons/installation-and-setup/

import uuid
import boto3
import os
import logging
from boto3 import session
from botocore.exceptions import ClientError

# low-level service access 
s3_client = boto3.client('s3') 

# oo way of working with low-level services 
s3_resource = boto3.resource('s3')

# function to generate randomized filename to improve storage performance
def create_bucket_name(bucket_prefix):
    #generated name should be 3 < name < 63 characters
    return''.join([bucket_prefix, str(uuid.uuid4())])

# function to create a bucket
def create_bucket(bucket_prefix, s3_connection):
    session = boto3.session.Session()
    current_region = session.region_name
    bucket_name = create_bucket_name(bucket_prefix)
    if current_region == 'us-east-1':
        bucket_response = s3_connection.create_bucket(
        Bucket = bucket_name)
    else:    
        bucket_response = s3_connection.create_bucket(
        Bucket = bucket_name,
        CreateBucketConfiguration = {
            'LocationConstraint':current_region})
    print(bucket_name, current_region)
    return bucket_name, bucket_response

# function to create a file to upload to s3 bucket
def create_temp_file(size, file_name, file_content):
    random_file_name = ''.join([str(uuid.uuid4().hex[:6]), file_name])
    with open(random_file_name,'w') as f:
        f.write(str(file_content)*size)
    return random_file_name

# function to upload a file to the s3 bucket
def upload_file(file_name, bucket, object_name=None):
    """Upload a file to an S3 bucket

    :param file_name: File to upload
    :param bucket: Bucket to upload to
    :param object_name: S3 object name. If not specified then file_name is used
    :return: True if file was uploaded, else False
    """

    # If S3 object_name was not specified, use file_name
    if object_name is None:
        object_name = os.path.basename(file_name)

    # Upload the file
    s3_client = boto3.client('s3')
    try:
        response = s3_client.upload_file(file_name, bucket, object_name)
    except ClientError as e:
        logging.error(e)
        return False
    return True
