import boto3 # type: ignore
'''
s3 = boto3.resource("s3")
for bucket in s3.buckets.all():
    print(bucket.name)
'''
# AWS credentials must be configured using `aws configure`
# This creates ~/.aws/credentials and ~/.aws/config files that boto3 uses automatically

class AWS:
    def __init__(self,service):
        self.service = service
    
    def get_connection(self):
        return boto3.client(self.service)

    def list_buckets(self):
        s3_client = self.get_connection()
        my_all_buck = []
        for bucket in s3_client.list_buckets()["Buckets"]:
            my_all_buck.append(bucket["Name"])
        return my_all_buck

    def create_bucket(self, name):
        s3_client = self.get_connection()
        response = s3_client.create_bucket(
        Bucket = name
        )
        if response["ResponseMetadata"]["HTTPStatusCode"] == 200:
            print(f"Bucket '{name}' created successfully")
        
    def delete_buckets(self, name):
        s3_client = self.get_connection()
        s3_client.delete_bucket(
        Bucket = name
        )

    def upload_file(self, bucket, file_path,key):
        s3_client = self.get_connection()
        s3_client.upload_file(
        file_path,
        bucket,
        key
        )

s3 = AWS('s3')

if __name__ == "__main__":  # Run the code below only if this file is executed directly, not when imported

    task = input("What do you want to do with bucket? Create, Delete or List \n").lower() 

    if task == "create":
        bucket_name = input("Enter name of your bucket: ")
        s3.create_bucket(bucket_name)

    elif task == "list":
        buckets = s3.list_buckets()
        if len(buckets) == 0: 
            print("No buckets founds!")
        else:
            print(f"These are your current buckets ")
            for buck in buckets:
                print(f"- {buck}")

    elif task == "delete":
        for buck in s3.list_buckets():
            print(f"- {buck}")
        bucket_name = input("Enter the bucket you want to delete among these ")
        s3.delete_buckets(bucket_name)   
        print(f"The bucket '{bucket_name}' has been deleted")
        
    else:
        pass

    while (int(input("Do you want to push json to s3 ? 0 or 1\n"))):
        s3.upload_file('check-test-python', 'output.json', 'json_logs') # Uploading a josn file to s3 bucket
        print("Uploaded")
        break
