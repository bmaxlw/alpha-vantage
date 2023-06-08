import yaml
from datetime import datetime

def parse_config(config_path: str) -> dict:
    with open(config_path, "r") as config:
        try:
            return yaml.safe_load(config)
        except yaml.YAMLError as YAMLExc:
            print(YAMLExc)
        except Exception as Exc:
            print(Exc)

def get_unique_time_id():
    return\
        str(datetime.now()).\
        replace('-', '').\
        replace(':', '').\
        replace('.', '').\
        replace(' ', '').\
        strip()