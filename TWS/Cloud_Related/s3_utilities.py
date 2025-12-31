import boto3 # type: ignore
'''
s3 = boto3.resource("s3")
for bucket in s3.buckets.all():
    print(bucket.name)
'''

def get_connection(service):
    return boto3.client(service)

def list_buckets(s3_client):
    my_all_buck = []
    print("These are your current buckets - ")
    for bucket in s3_client.list_buckets()["Buckets"]:
        my_all_buck.append(bucket["Name"])
    return my_all_buck

def create_bucket(s3_client,name):
    s3_client.create_bucket(
    Bucket = name
    )
    
def delete_buckets(s3_client, buckets):
    for bucket in buckets:
        if bucket == "check-test-python":
            continue
        else:
            s3_client.delete_bucket(
                Bucket = bucket
            )

s3 = get_connection("s3")

task = input("What do you want to do with bucket? Create, Delete or List ").lower()
if task == "create":
    bucket_name = input("Enter name of your bucket: ")
    create_bucket(s3,bucket_name)
    print("Bucket create successfully")
elif task == "list":
    list_buckets(s3)
elif task == "delete":
    list_buckets(s3)
    bucket_name = input("Enter the bucket you want to delete among these: ")
    delete_buckets(s3, bucket_name)
else:
    pass

# buckets = list_buckets(s3)

# delete_buckets(s3,buckets) - Deleting all buckets for now