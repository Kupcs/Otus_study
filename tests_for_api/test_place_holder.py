from api_testing.base_request import BaseRequest
import pytest
import requests


URL_CREATE_RESOURCE = "https://jsonplaceholder.typicode.com/posts"
DEL_RESOURCE = "https://jsonplaceholder.typicode.com/posts/1"


@pytest.mark.parametrize("url",[("url_1"), ("url_2"), ("url_3"), ("url_4")])
def test_system_check(urls_for_checking_place_status_code, url):
    url = urls_for_checking_place_status_code(url=url)
    response = BaseRequest(url)
    assert response.check_status_code("GET") == 200, "Status code is not 200"

def test_create_resource():
    data = {'title':'foo',
            'body':'bar',
            'userId':'1'}
    response = BaseRequest(URL_CREATE_RESOURCE)
    response_body = (response.check_json("POST", data))['body']
    response_title = (response.check_json("POST", data))['title']
    response_user_id = (response.check_json("POST", data))['userId']
    assert response_body == 'bar'
    assert response_user_id == '1'
    assert response_title == 'foo'


def test_del_resource():
    response = requests.delete(DEL_RESOURCE)
    assert response.status_code == 200, "Delete is not success"

@pytest.mark.parametrize(("url", "user_id"),
                         [("user_id_3", 3), ("user_id_4", 4),
                          ("user_id_10", 10), ("user_id_5", 5)]
                         )
def test_rout_resource(urls_for_checking_place_rout, url, user_id):
    url = urls_for_checking_place_rout(url = url)
    response = BaseRequest(url)
    for i in response.check_json("GET"):
        assert i['userId'] == user_id




