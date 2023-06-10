import requests

URL = "http://datamall2.mytransport.sg/ltaodataservice/CarParkAvailabilityv2?$skip="
API_KEY = "8pjsOFa5RpeLxuoRbBM2Eg=="


def get_available_lots(url= URL, api_key=API_KEY):
    """
    Retrieves current available parking lots
    """

    headers = {
    'AccountKey': API_KEY
    }

    response = requests.request("GET", URL, headers=headers)

    if response.status_code == 200:
        return print(response.json())
    else:
        print('failed to retrieve file')


if __name__ == "__main__":
    get_available_lots()