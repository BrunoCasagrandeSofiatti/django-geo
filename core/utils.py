import requests
from random import randint
from django.conf import settings
from django.contrib.gis.geoip2 import GeoIP2
from django.contrib.gis.geoip2 import geoip2



YELP_SEARCH_ENDPOIT = 'http://api.yelp.com/v3/businesses/search'

def yelp_search(keyword=None, location=None):
    headers = {"Authorization": "Bearer " + settings.YELP_API_KEY}

    if keyword and location:
        parms = {'term': keyword, 'location': location}
    else:
        parms = {'term': 'Pizzaria', 'location': 'Rio Verde'}

    r = requests.get(YELP_SEARCH_ENDPOIT, headers=headers, params=parms)

    return r.json()

def get_client_city_data():
    g = GeoIP2()
    ip = get_randow_ip()
    try:
        return g.city(ip)
    except:
        return None

def get_randow_ip():
    return '.'.join([str(randint(0,255)) for x in range(4)])