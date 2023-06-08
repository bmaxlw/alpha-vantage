import json

class ResponseFormatter:
    
    def format_response(self, responses) -> list:
        formatted_response_list = []
        for response in responses:
            json_response = json.loads(response)
            json_keys = [_ for _ in json_response.keys()]
            for json_key, json_value in json_response.get(json_keys[0]).items():
                symbol = json_value if json_key.split('.')[1].strip().lower() == "symbol" else None
                if symbol:
                    for key, value in json_response.get(json_keys[1]).items():
                        datetime_str=f"\"datetime\": \"{key}\", \"symbol\": \"{symbol}\", "
                        data_str=f"""{', '.join([f'"{k.split(".")[1].strip()}": {v}' for k, v in value.items()])}"""
                        final_str="{"+datetime_str+data_str+"}"
                        formatted_response_list.append(final_str)
        return formatted_response_list

                    

