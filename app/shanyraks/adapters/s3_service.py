from typing import BinaryIO

import boto3

class S3Service:
    def __init__(self):
        self.s3 = boto3.client("s3")

    def upload_file(self, shanyrak_id: str, file: BinaryIO, filename: str):
        bucket = "myprojectsecret01-bucket"
        filekey = f"shanyraks/{shanyrak_id}/media/{filename}"

        self.s3.upload_fileobj(file, bucket, filekey)

        bucket_location = boto3.client("s3").get_bucket_location(
            Bucket = bucket
        )
        object_url = f'https://s3-{bucket_location["LocationConstraint"]}.amazonaws.com/{bucket}/{filekey}'

        return object_url