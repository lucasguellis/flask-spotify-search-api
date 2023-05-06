def is_token_expired(result):
    if "error" in result.json() and result.json()['error']['message'] == "The access token expired":
        return True
    return False
