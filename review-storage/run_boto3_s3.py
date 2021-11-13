import boto3
from boto3_s3 import create_bucket, upload_file
s3_resource = boto3.resource('s3')

first_bucket_name, first_response = create_bucket(
    bucket_prefix='firstpythonbucket',
    s3_connection=s3_resource.meta.client)

# output in terminal:
#firstpythonbucket62ae4bdf-3a7e-41c1-8fa7-70ceb963e654 us-east-1
#first_response
#{'ResponseMetadata': {'RequestId': 'X1TSBP9PM668NE72',...
# Dict reponse

second_bucket_name, second_response = create_bucket(
    bucket_prefix='secondpythonbucket',
    s3_connection=s3_resource)  
#resource interface
#output: secondpythonbucket958d7913-260e-4e39-89b6-7a1f2962c095 us-east-1
#second_response
#s3.Bucket(name='secondpythonbucket958d7913-260e-4e39-89b6-7a1f2962c095')
#s3 Bucket response

from boto3_s3 import create_temp_file
first_file_name = create_temp_file(300, 'firstfile.txt','f')
#output: 4e6733firstfile.txt
# we need to randomize file names to prevent slowing down when 
# multiple similar prefixed files are accessed as they are stored together by default

upload_file('review-processing/reviews.csv', 
            'reviews2ce7b345-0e23-4d01-ac84-e2ea6def5d65', object_name=None)

upload_file('/Users/karshi/Documents/GitHub/review-management-pipeline/review-processing/sampled_reviews.csv', 
            'reviews2ce7b345-0e23-4d01-ac84-e2ea6def5d65', object_name=None)