from api_testing.base_request import BaseRequest
import pytest


"""Number of breweries to return each call.Note: Default is 1. Max per page is 50."""
URL_BREW_SIZE = "https://api.openbrewerydb.org/v1/breweries/random?size=50"
""""Show USA breweries meta data"""
URL_META_DATA = "https://api.openbrewerydb.org/v1/breweries/meta?by_country=united_states"
"""Show all breweries meta data"""
URL_ALL_META = "https://api.openbrewerydb.org/v1/breweries/meta"

@pytest.mark.parametrize("url",[("url_1"), ("url_2"), ("url_3"), ("url_4")])
def test_check_status_code(urls_for_checking_brews_status_code, url):
    url = urls_for_checking_brews_status_code(url=url)
    response = BaseRequest(url)
    assert response.check_status_code("GET") == 200, "Status code is not 200"

@pytest.mark.parametrize(("url", "city"),
                         [("url_san_diego", "San Diego"), ("url_san_norman", "Norman"),
                          ("url_san_austin", "Austin"), ("url_san_mason","Mason")])
def test_check_filter_by_city(urls_for_checking_cities, url, city):
    url = urls_for_checking_cities(url = url)
    response = BaseRequest(url)
    response_city = (response.check_json("GET"))[0]['city']
    assert response_city == city, f"Response_city is not {city}"

def test_brew_size():
    response = BaseRequest(URL_BREW_SIZE)
    assert len(response.check_json("GET")) == 50

def test_meta_data():
    response = BaseRequest(URL_META_DATA)
    assert response.check_json("GET")['total'] == '7967'

def test_all_meta_data():
    response = BaseRequest(URL_ALL_META)
    assert response.check_json("GET")['total'] == '8237'
