from operator import ge
import urllib.request 
import json
from pprint import pprint
from API_KEY.config import MAPQUEST_API_KEY, MBTA_API_KEY

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
    # lat_lng = response_data['results'][0]['locations'][0]['latLng']['lat']['latLng']['lng']
    # normal_name = place_name.replace('%20', ' ')
    # return(f'The coordinates for {normal_name} are {(lat, lng)}.')
    return lat, lng
    

def get_nearest_station(latitude, longitude):
    """
    Given latitude and longitude strings, return a (station_name, wheelchair_accessible)
    tuple for the nearest MBTA station to the given coordinates.
    See https://api-v3.mbta.com/docs/swagger/index.html#/Stop/ApiWeb_StopController_index for URL formatting requirements for the 'GET /stops' API.
    """
    lat = str(latitude)
    long = str(longitude)
    # return lat, long

    url = f'https://api-v3.mbta.com/stops?api_key={MBTA_API_KEY}&sort=distance&filter%5Blatitude%5D={latitude}&filter%5Blongitude%5D={longitude}'
    response_data = get_json(url)
    # print(response_data)

    station_name = response_data['data'][0]['attributes']['name']
    wheelchair_accessible = response_data['data'][0]['attributes']['wheelchair_boarding']

    if wheelchair_accessible == 2: 
        wheelchair_accessible = 'This station is not wheelchair accessible.'
        return(f'{station_name}: {wheelchair_accessible}.')
    elif wheelchair_accessible == 1: 
        wheelchair_accessible = 'This station is wheelchair accessible'
        return(f'{station_name}: {wheelchair_accessible}.')
    else: 
        wheelchair_accessible = 'There is no information on wheelchair accessiblity.'
        return(f'{wheelchair_accessible} for the MBTA stop {station_name}.')


def find_stop_near(place_name):
    """
    Given a place name or address, return the nearest MBTA stop and whether it is wheelchair accessible.

    This function might use all the functions above.
    """
    get_lat_long(place_name)
    lat = get_lat_long(place_name)[0]
    long = get_lat_long(place_name)[1]
    return get_nearest_station(lat, long)


def main():
    """
    You can test all the functions here
    """
    # print(get_json(f'http://www.mapquestapi.com/geocoding/v1/address?key={MAPQUEST_API_KEY}&location=Babson%20College'))
    # get_lat_long('Babson%20College')
    # print(get_lat_long('Babson%20College'))

    address = '656 Tremont St Boston'
    address_in_format = address.replace(' ','%20')

    # lat_long = get_lat_long(address)
    # print(lat_long)

    # lat = str(get_lat_long(address)[0])
    # long = str(get_lat_long(address)[1])
    # print(get_nearest_station(lat, long)) 

    nearest_stop = find_stop_near(address_in_format)
    print(f'The nearest stop to {address} is on {nearest_stop}')

main()
