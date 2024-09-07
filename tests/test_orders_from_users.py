import allure
import requests
from data import Data
from helpers import *


class TestGetListOrder:
    @allure.title('Проверяем получения списка заказов c авторизованным пользователем')
    @allure.description(
        'Проверяем получение списка заказов, получаем статус 200')
    def test_get_list_order_200(self):
        user = {
            'email': create_email_user_random(),
            'password': create_user_pass_random(),
            'name': create_user_name_random()
        }
        requests.post(Data.create_user, data=user)
        login = requests.post(Data.login_user, data=user)
        token = login.json()['accessToken']
        response = requests.get(Data.orders_from_user, headers={'Authorization': token}, data=user)
        assert response.status_code == 200

    @allure.title('Проверяем получения списка заказов c неавторизованным пользователем')
    @allure.description(
        'Проверяем получение списка заказов, получаем статус 401')
    def test_get_list_order_401(self):
        user = {
            'email': create_email_user_random(),
            'password': create_user_pass_random(),
            'name': create_user_name_random()
        }
        requests.post(Data.create_user, data=user)
        response = requests.get(Data.orders_from_user, data=user)
        assert (response.status_code == 401
                and response.json()["success"] == False
                and response.json()["message"] == "You should be authorised")