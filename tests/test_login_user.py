import allure
import requests
from data import Data, UserData, ResponseMessages
from helpers import *


class TestLoginUser:
    @allure.title('Проверка валидного логина пользователя')
    @allure.description(
        'Создаём аккаунт пользователя и логинимся на него, получаем статус 200')
    def test_user_login_passed(self):
        payload = {'email': UserData.email,
                   'password': UserData.password,
                   'name': UserData.name
                   }
        response = requests.post(Data.login_user, data=payload)
        del payload["password"]
        assert (response.status_code == 200
                and response.json()["success"] == True
                and response.json()["user"] == payload)

    @allure.title('Проверка c невалидным логином')
    @allure.description(
        'Пытаемся залогиниться в аккаунт пользователя, получаем ошибку 401')
    def test_no_such_login(self):
        payload = {'email': UserData.incorrect_login,
                   'password': create_user_pass_random(),
                   'name': create_user_name_random()
                   }
        response = requests.post(Data.login_user, data=payload)
        assert (response.status_code == 401
                and response.json()["success"] == False
                and response.json()["message"] == ResponseMessages.incorrect_data)

    @allure.title('Проверка логина c неверным паролем')
    @allure.description(
        'Пытаемся залогиниться в аккаунт пользователя, получаем ошибку 401')
    def test_no_such_password(self):
        payload = {'email': create_email_user_random(),
                   'password': UserData.incorrect_password,
                   'name': create_user_name_random()
                   }
        response = requests.post(Data.login_user, data=payload)
        assert (response.status_code == 401
                and response.json()["success"] == False
                and response.json()["message"] == ResponseMessages.incorrect_data)