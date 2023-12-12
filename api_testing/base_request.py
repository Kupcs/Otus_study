import requests

class BaseRequest:
    def __init__(self, base_url):
        self.base_url = base_url

    def response(self, request_type, payload = None):
        if request_type == "GET":
            response = requests.get(self.base_url)
        else:
            response = requests.post(self.base_url, data = payload)
        return response

    def check_status_code(self, request_type):
        """метод для получения статус кода"""
        return self.response(request_type).status_code

    def check_json(self, request_type, payload = None):
        """метод для получения json"""
        return self.response(request_type, payload).json()

