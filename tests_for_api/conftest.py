import pytest

@pytest.fixture
def urls_for_checking_message():
    def _wrapper(url: str):
            if url == "url_1":
                return "https://dog.ceo/api/breeds/list/all"
            if url == "url_2":
                return "https://dog.ceo/api/breeds/image/random"
            if url == "url_3":
                return "https://dog.ceo/api/breeds/image/random/3"
            if url == "url_4":
                return "https://dog.ceo/api/breeds/image/random/52"

    yield _wrapper

@pytest.fixture
def urls_for_checking_brews_status_code():
    def _wrapper(url: str):
            if url == "url_1":
                return "https://api.openbrewerydb.org/v1/breweries/5128df48-79fc-4f0f-8b52-d06be54d0cec"
            if url == "url_2":
                return "https://api.openbrewerydb.org/v1/breweries?by_city=san_diego"
            if url =="url_3":
                return "https://api.openbrewerydb.org/v1/breweries/meta?by_country=united_states"
            if url == "url_4":
                return "https://api.openbrewerydb.org/v1/breweries/meta?by_country=united_states"
            if url == "url_5":
                return "https://api.openbrewerydb.org/v1/breweries/meta"
    yield _wrapper

@pytest.fixture
def urls_for_checking_cities():
    """Filter breweries by city"""
    def _wrapper(url: str):
            if url == "url_san_diego":
                return "https://api.openbrewerydb.org/v1/breweries?by_city=san_diego"
            if url == "url_san_norman":
                return "https://api.openbrewerydb.org/v1/breweries?by_city=norman"
            if url == "url_san_austin":
                return "https://api.openbrewerydb.org/v1/breweries?by_city=austin"
            if url == "url_san_mason":
                return "https://api.openbrewerydb.org/v1/breweries?by_city=mason"
    yield _wrapper

@pytest.fixture
def urls_for_checking_place_status_code():
    def _wrapper(url: str):
            if url == "url_1":
                return "https://api.openbrewerydb.org/v1/breweries/random?size=50"
            if url == "url_2":
                return "https://jsonplaceholder.typicode.com/posts"
            if url =="url_3":
                return "https://jsonplaceholder.typicode.com/posts?userId=3"
            if url == "url_4":
                return "https://api.openbrewerydb.org/v1/breweries/meta?by_country=united_states"
            if url == "url_5":
                return "https://api.openbrewerydb.org/v1/breweries/meta"
    yield _wrapper


@pytest.fixture
def urls_for_checking_place_rout():
    """Basic filtering is supported through query parameters."""
    def _wrapper(url: str):
            if url == "user_id_3":
                return "https://jsonplaceholder.typicode.com/posts?userId=3"
            if url == "user_id_4":
                return "https://jsonplaceholder.typicode.com/posts?userId=4"
            if url == "user_id_10":
                return "https://jsonplaceholder.typicode.com/posts?userId=10"
            if url == "user_id_2":
                return "https://jsonplaceholder.typicode.com/posts?userId=2"
            if url == "user_id_5":
                return "https://jsonplaceholder.typicode.com/posts?userId=5"
    yield _wrapper


def pytest_addoption(parser):
    parser.addoption('--url', action = "store", default="https://ya.ru", help="my option: type1 or type2")
    parser.addoption('--status_code', action="store", default="200", help="my option: type1 or type2")


@pytest.fixture
def fix_url(request):
    url = request.config.getoption('--url')
    return url

@pytest.fixture
def fix_status(request):
    status_code =  request.config.getoption('--status_code')
    return status_code