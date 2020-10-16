import requests


def make_get_request(url):
    '''
    send a GET request

            Parameters:
                    url (string): url from which is being made
            Returns:
                    json response(json): Json response
    '''
    response = requests.get(url).json()
    return response