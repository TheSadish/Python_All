import boto3 # type: ignore
'''
s3 = boto3.resource("s3")
for bucket in s3.buckets.all():
    print(bucket.name)
'''
# AWS credentials must be configured using `aws configure`
# This creates ~/.aws/credentials and ~/.aws/config files that boto3 uses automatically


def get_connection(service):
    return boto3.client(service)

def list_buckets(s3_client):
    my_all_buck = []
    for bucket in s3_client.list_buckets()["Buckets"]:
        my_all_buck.append(bucket["Name"])
    return my_all_buck

def create_bucket(s3_client,name):
    response = s3_client.create_bucket(
    Bucket = name
    )
    if response["ResponseMetadata"]["HTTPStatusCode"] == 200:
        print(f"Bucket '{name}' created successfully")
    
def delete_buckets(s3_client, bucket):
    s3_client.delete_bucket(
    Bucket = bucket
    )

def upload_file(s3_client, bucket, file_path,key):
    s3_client.upload_file(
    file_path,
    bucket,
    key
    )

s3 = get_connection("s3")

task = input("What do you want to do with bucket? Create, Delete or List \n").lower() 

if task == "create":
    bucket_name = input("Enter name of your bucket: ")
    create_bucket(s3,bucket_name)

elif task == "list":
    buckets = list_buckets(s3)
    if len(buckets) == 0: 
        print("No buckets founds!")
    else:
        print(f"These are your current buckets ")
        for buck in buckets:
            print(f"- {buck}")

elif task == "delete":
    for buck in list_buckets(s3):
        print(f"- {buck}")
    bucket_name = input("Enter the bucket you want to delete among these ")
    delete_buckets(s3, bucket_name)   
    print(f"The bucket '{bucket_name}' has been deleted")
    
else:
    pass

if (input("Do you want to push to s3 ? 0 or 1\n")):
    upload_file(s3, 'check-test-python', 'output.json', 'json_logs') # Uploading a josn file to s3 bucket
    print("Uploaded")