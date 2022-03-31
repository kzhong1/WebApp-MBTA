import urllib.request 
import json
from pprint import pprint

MAPQUEST_API_KEY = '7VwoBd57eTpyIl5xXGGaqY91XyMVsZI6'

# Useful URLs (you need to add the appropriate parameters for your requests)
MAPQUEST_BASE_URL = "http://www.mapquestapi.com/geocoding/v1/address"
MBTA_BASE_URL = "https://api-v3.mbta.com/stops"


def get_json(url):
    """
    Given a properly formatted URL for a JSON web API request, return
    a Python JSON object containing the response to that request.

    Both get_lat_long() and get_nearest_station() might need to use this function.
    """

    f = urllib.request.urlopen(url)
    response_text = f.read().decode('utf-8')
    response_data = json.loads(response_text)
    return response_data


def get_lat_long(place_name):
    """
    Given a place name or address, return a (latitude, longitude) tuple
    with the coordinates of the given place.
    See https://developer.mapquest.com/documentation/geocoding-api/address/get/
    for Mapquest Geocoding API URL formatting requirements.
    """
    url = f'http://www.mapquestapi.com/geocoding/v1/address?key={MAPQUEST_API_KEY}&location={place_name}'
    # print(get_json(url))
    response_data = get_json(url)
    lat = response_data['results'][0]['locations'][0]['latLng']['lat']
    lng = response_data['results'][0]['locations'][0]['latLng']['lng']
    normal_name = place_name.replace('%20', ' ')
    return(f'The coordinates for {normal_name} are {(lat, lng)}.')

def get_nearest_station(latitude, longitude):
    """
    Given latitude and longitude strings, return a (station_name, wheelchair_accessible)
    tuple for the nearest MBTA station to the given coordinates.
    See https://api-v3.mbta.com/docs/swagger/index.html#/Stop/ApiWeb_StopController_index for URL formatting requirements for the 'GET /stops' API.
    """
    url = f'https://api-v3.mbta.com/docs/swagger/index.html#/Stop/ApiWeb_StopController_index/GET%20/stops'
    response_data = get_json(url)
    print(response_data)


def find_stop_near(place_name):
    """
    Given a place name or address, return the nearest MBTA stop and whether it is wheelchair accessible.

    This function might use all the functions above.
    """
    pass


def main():
    """
    You can test all the functions here
    """
    pass


if __name__ == '__main__':
    main()
    # get_json(f'http://www.mapquestapi.com/geocoding/v1/address?key={MAPQUEST_API_KEY}&location=Babson%20College')
    get_lat_long('Babson%20College')
    # print(get_lat_long('Babson%20College'))
    get_nearest_station(1, 2)