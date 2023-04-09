import requests

from common.json_methods import create_json_file


class Common:
    def __init__(self, head_url, token):
        """
        Инициализация параметров для авторизации.
        :param head_url: Начальная ссылка
        :param token: Токен
        """
        self.verify = False  # should be True (SSL problem)
        self.head_url = head_url
        self.token = token
        self.parent_dir_response = 'RESPONSES'
        self.parent_dir_request = 'REQUESTS'
        self.headers_auth = {"Authorization": f"Bearer {self.token}"}

        self.get_examples = "get_examples"
        self.post_examples = "post_examples"
        self.put_examples = "put_examples"
        self.del_examples = "del_examples"

    def get_response(self, filename, postfix, data=''):
        """
        Метод собирает все необходимые данные для GET запроса и сохраняет их в файл JSON.
        """
        method = "GET"
        url = self.head_url + postfix
        response = requests.request(method, url, headers=self.headers_auth, data=data, verify=self.verify)
        info = create_json_file(response, filename, method, self.parent_dir_response)
        print("GET Response status code:", response.status_code)
        return info

    def post_response(self, filename, postfix, data=''):
        """
        Метод собирает все необходимые данные для POST запроса и сохраняет полученные данные в файл JSON.
        """
        method = "POST"
        url = self.head_url + postfix
        response = requests.request(method, url, headers=self.headers_auth, data=data, verify=self.verify)
        info = create_json_file(response, filename, method, self.parent_dir_response)
        print("POST Response status code:", response.status_code)
        return info

    def put_response(self, filename, postfix, data=''):
        """
        Метод собирает все необходимые данные для PUT запроса и сохраняет полученные данные в файл JSON.
        """
        method = "PUT"
        url = self.head_url + postfix
        response = requests.request(method, url, headers=self.headers_auth, data=data, verify=self.verify)
        info = create_json_file(response, filename, method, self.parent_dir_response)
        print("PUT Response status code:", response.status_code)
        return info

    def refresh_token(self):
        """
        Метод обновляет токен. Возвращает дату валидности токена.
        """
        file_name = "oauth_refresh_info.json"
        postfix = '/oauth/refresh'
        refresh_info = self.post_response(file_name, postfix)
        return refresh_info

    def get_auth_info(self):
        """
        Авторизация и получение данных о клиенте (login, ID, 2fa etc.)
        """
        file_name = "auth_info.json"
        postfix = '/auth'
        auth_info = self.get_response(file_name, postfix)
        print('Auth - OK')
        return auth_info
