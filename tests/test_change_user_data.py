import allure
import requests
from data import Data
from helpers import *

class TestChangeUserData:
    @allure.title('Проверяем изменения данных пользователя с авторизацией')
    @allure.description('Создаем аккаунт пользователя, заходим на него и изменяем данные')
    def test_change_user_data_from_authorization(self):
        user_1 = {'email': create_email_user_random(),
                  'password': create_user_pass_random(),
                  'name': create_user_name_random()
                  }
        user_2 = {'email': create_email_user_random(),
                  'password': create_user_pass_random(),
                  'name': create_user_name_random()
                  }
        requests.post(Data.create_user, data=user_1)
        user_data = requests.post(Data.login_user, data=user_1)
        token = user_data.json()['accessToken']
        response = requests.patch(Data.change_user_data, headers={'Authorization': token}, data=user_2)
        assert response.status_code == 200 and user_data.json()['user']['email'] != response.json()['user']['email'] \
        and user_data.json()['user']['name'] != response.json()['user']['name']

    @allure.title('Проверяем изменения данных пользователя без авторизации')
    @allure.description('Изменяем данные пользователя без авторизации, ожидаем получение ошибки')
    def test_change_user_data_without_authorization(self):
        user_1 = {'email': create_email_user_random(),
                  'password': create_user_pass_random(),
                  'name': create_user_name_random()
                  }
        user_2 = {'email': create_email_user_random(),
                  'password': create_user_pass_random(),
                  'name': create_user_name_random()
                  }
        requests.post(Data.create_user, data=user_1)
        response = requests.patch(Data.change_user_data, data=user_2)
        assert response.status_code == 401 and response.json()['message'] == "You should be authorised"