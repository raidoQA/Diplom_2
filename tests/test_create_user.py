import allure
import requests
from data import Data, UserData
from helpers import *


class TestUserCreate:
    @allure.title('Проверяем создания пользователя')
    @allure.description('Создаём пользователя и проверяем, что код ответа = 200')
    def test_create_user(self):
        payload = {'email': create_email_user_random(),
                   'password': create_user_pass_random(),
                   'name': create_user_name_random()
                   }
        response = requests.post(Data.create_user, data=payload)
        del payload["password"]
        assert (response.status_code == 200
                and response.json()["success"] == True
                and response.json()["user"] == payload)

    @allure.title('Проверяем создания пользователя, который уже есть')
    @allure.description('Создаём пользователя и проверяем, что код ответа = 403')
    def test_duplicate_create_user(self):
        payload = {'email': UserData.email,
                   'password': create_user_pass_random(),
                   'name': create_user_name_random()
                   }
        response = requests.post(Data.create_user, data=payload)
        assert (response.status_code == 403
                and response.json()["success"] == False
                and response.json()["message"] == "User already exists")


    @allure.title('Проверяем невозможность создания пользователя без одного обязательного поля')
    @allure.description('Проверяем создание аккаунта без пароля, получаем ошибку 403')
    def test_not_once_required_field(self):
        payload = {'email': create_email_user_random(),
                   'name': create_user_name_random()
                   }
        response = requests.post(Data.create_user, data=payload)
        assert (response.status_code == 403
                and response.json()["success"] == False
                and response.json()["message"] == "Email, password and name are required fields")