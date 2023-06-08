import os
from utils import parse_config
from src.api_getter import APIGetter
from src.response_formatter import ResponseFormatter
from src.data_loader import DataLoader
from src.aws_handler import AWSHandler

if __name__ == "__main__":
    environment  = os.environ.get("ENVIRONMENT", "dev")
    config_path  = os.environ.get("CONFIG_PATH", "config.yaml")
    aws_location = os.environ.get("AWS_DEFAULT_LOCATION")
    if all([environment, config_path, aws_location]):
        config       = parse_config(config_path).get(environment)
        bucket_name  = config.get("aws_s3_bucket_name")
        getter       = APIGetter()
        formatter    = ResponseFormatter()
        handler      = AWSHandler()
        loader       = DataLoader()
        try:
            urls          = getter.concat_urls_from_config(url_params=config)
            responses     = getter.get_api_endpoint(urls=urls)
            response_list = formatter.format_response(responses=responses)
            session       = handler.create_AWS_session()
            handler.create_S3_bucket(S3_bucket_name=bucket_name, 
                                     location=aws_location)
            loader.load_data_to_S3_bucket(session=session, 
                                          bucket_name=bucket_name, 
                                          response_list=response_list)
        except AttributeError as attr_error:
            print(f"... {attr_error} ...")
        except Exception as exc:
            print(f"... {exc} ...")
    else:
        print("... Environment variables are not properly set up ...")
