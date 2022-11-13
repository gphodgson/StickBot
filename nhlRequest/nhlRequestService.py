import requests

class nhlRequestService():
    URI_STEM = 'https://statsapi.web.nhl.com/api/v1/'

    def __init__(self) -> None:
        pass

    def makeGetRequest(self, extension, params):
        headers = {}

        http_response = requests.get(
            self.URI_STEM + extension,
            headers=headers,
            params=params
            )
        
        return http_response.json()