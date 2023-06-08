import json
from boto3 import Session
from utils import get_unique_time_id

class DataLoader:

    def load_data_to_S3_bucket(self, 
                               session: Session, 
                               bucket_name: str,
                               response_list: list=[]) -> None:
        s3 = session.resource('s3')
        if len(response_list) > 0:
            for json_document in response_list:
                s3_dir = json.loads(json_document).get("symbol")
                s3_object = s3.Object(bucket_name=bucket_name, 
                                      key=f'{s3_dir}/{s3_dir}_{get_unique_time_id()}.json')
                s3_object.put(Body=json_document)
        else: 
            print("... Response list is empty, no load required ...")
