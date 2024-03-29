import requests


from ..utils.treatments import dict_to_url_params, filter_result
from ..utils.validations import is_token_expired
from .token import Token


class Search:
    def __init__(self, args):
        self.dict_args = args

        self.BASE_URL = "https://api.spotify.com/v1/search/" + dict_to_url_params(args)
        self.token = Token.get_actual_token()

    @property
    def headers(self):
        return {"Authorization": f"Bearer  {self.token}"}

    def search(self):
        result = requests.get(self.BASE_URL, headers=self.headers)
        if is_token_expired(result):
            new_token = Token().get_new_token()
            self.token = new_token

        result = requests.get(self.BASE_URL, headers=self.headers)
        filtered_result = filter_result(['album_group', 'album_type', 'artists', 'href', 'id', 'images', 'name', 'release_date', 'release_date_precision', 'total_tracks', 'type', 'uri'], result.json()['albums']['items'][0])
        return filtered_result
