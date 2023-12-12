from api_testing.base_request import BaseRequest
import pytest

URL_DOG_RANDOM_IMAGE = "https://dog.ceo/api/breeds/image/random"
URL_DOG_RANDOM_IMAGES ="https://dog.ceo/api/breeds/image/random/3"
URL_DOG_RANDOM_IMAGES_MAX ="https://dog.ceo/api/breeds/image/random/52"


@pytest.mark.parametrize("urls",
                         ["https://dog.ceo/api/breeds/list/all", "https://dog.ceo/api/breeds/image/random",
                            "https://dog.ceo/api/breeds/image/random/3", "https://dog.ceo/api/breeds/image/random/52"
                            ])
def test_dogs_status_code(urls):
    """"Тест на ответ сервера"""
    response = BaseRequest(urls)
    assert response.check_status_code("GET") == 200, "Status code is not 200"

@pytest.mark.parametrize("url",[("url_1"), ("url_2"), ("url_3"), ("url_4")])
def test_dogs_message(urls_for_checking_message, url):
    """"Тест на ответ сервера, сообщение не пустое"""
    url = urls_for_checking_message(url=url)
    response = BaseRequest(url)
    assert len(response.check_json("GET")['message']) > 0, "Message is none"

def test_jpg_in_image():
    """"Тест на то, что в ответе сервера есть файл с изображением"""
    response = BaseRequest(URL_DOG_RANDOM_IMAGE)
    assert ".jpg" in response.check_json("GET")['message'], "There is no .jpg file in the response"

def test_check_images_count():
    """"Тест проверяющий количество запроешенных собак"""
    response = BaseRequest(URL_DOG_RANDOM_IMAGES)
    assert len(response.check_json("GET")['message']) == 3, "Elements(dogs) count in not equal"

def test_max_amount_of_dogs():
    """"Тест проверяющий максимальное количество запрашиваемых собак собак"""
    response = BaseRequest(URL_DOG_RANDOM_IMAGES_MAX)
    assert len(response.check_json("GET")['message']) == 50, "Elements(dogs) count in not equal"







