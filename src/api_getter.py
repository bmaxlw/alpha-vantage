import os, requests

class APIGetter:

    def concat_urls_from_config(self, url_params: dict) -> list:
        base_url   = url_params.get("base_url")
        apikey     = f"&apikey={os.environ.get('API_KEY')}"
        params     = '&'.join([f'{k}={v}' for k, v in url_params.get("url_params").items()])
        final_urls = []
        for symbol in url_params.get("symbol"):
            final_url = f"{base_url}{params}&symbol={symbol}{apikey}"
            final_urls.append(final_url)
        return final_urls
    
    def get_api_endpoint(self, urls: list) -> list:
        responses = [] 
        for url in urls:
            response = requests.get(url=url)
            responses.append(response.text)
        return responses
