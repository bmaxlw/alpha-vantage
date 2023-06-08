import os
from boto3 import Session
from botocore.client import ClientError

class AWSHandler:

    def __init__(self) -> None:
        self.__aws_access_key_id     = os.getenv("AWS_ACCESS_KEY_ID")
        self.__aws_secret_access_key = os.getenv("AWS_SECRET_ACCESS_KEY")

    def create_AWS_session(self) -> Session:
        session = Session(
            aws_access_key_id=self.__aws_access_key_id,
            aws_secret_access_key=self.__aws_secret_access_key)
        return session

    def create_S3_bucket(self, S3_bucket_name: str, location: str) -> None:
        session = self.create_AWS_session()
        s3 = session.resource('s3')
        try:
            s3.meta.client.head_bucket(Bucket=S3_bucket_name)
        except ClientError:
            s3.create_bucket(Bucket=S3_bucket_name, 
                             CreateBucketConfiguration={'LocationConstraint': location})