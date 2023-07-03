def dict_to_url_params(d: dict) -> str:
    """
    Converts a dictionary to a string in the format of URL parameters.
    """
    # Initialize an empty list to store the key-value pairs
    params = []
    # Loop through the dictionary and convert each key-value pair to a string
    for key, value in d.items():
        # If the value is a list, join the elements with commas
        if isinstance(value, list):
            value = ",".join(value)
        # Append the key-value pair to the list
        params.append(f"{key}={value}")
    # Join the key-value pairs with ampersands and add a question mark at the beginning
    return "?" + "&".join(params)


def filter_result(keys: list, result: dict) -> dict:
    return {key: result[key] for key in keys if key in result}
