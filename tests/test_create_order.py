import allure
import requests
from data import Data, BurgerIngredients
from helpers import *


class TestCreateOrder:
    @allure.title('Проверяем создание заказа с ингредиентами под авторизованным пользователем')
    @allure.description(
        'При создании заказа передаются существующие ингредиенты авторизованным пользователем')
    def test_create_order_ingredients_authorized_user(self):
        user = {'email': create_email_user_random(),
                'password': create_user_pass_random(),
                'name': create_user_name_random()
                }
        requests.post(Data.login_user, data=user)
        response = requests.post(Data.create_order, data=BurgerIngredients.burger_existing)
        assert (response.status_code == 200
                and response.json()["success"] == True
                and response.json()["name"] == BurgerIngredients.burger_existing_check)

    @allure.title('Проверяем создание заказа с ингредиентами под неавторизованным пользователем')
    @allure.description('При создании заказа передаются существующие ингредиенты неавторизованным пользователем')
    def test_create_order_ingredients_unauthorized_user(self):
        user = {'email': create_email_user_random(),
                'password': create_user_pass_random(),
                'name': create_user_name_random()
                }
        requests.post(Data.login_user, data=user)
        response = requests.post(Data.create_order, data=BurgerIngredients.burger_existing)
        assert (response.status_code == 200
                and response.json()["success"] == True
                and response.json()["name"] == BurgerIngredients.burger_existing_check)

    @allure.title('Проверяем создание заказа без ингредиентов')
    @allure.description('При создании заказа не передаются ингредиенты ')
    def test_create_order_authorized_user_no_ingredients(self):
        user = {'email': create_email_user_random(),
                'password': create_user_pass_random(),
                'name': create_user_name_random()
                }
        requests.post(Data.login_user, data=user)
        response = requests.post(Data.create_order, data=BurgerIngredients.burger_empty)
        assert (response.status_code == 400
                and response.json()["success"] == False
                and response.json()["message"] == "Ingredient ids must be provided")

    @allure.title('Проверяем создание заказа с неверным хешем ингредиентов авторизованным пользователем')
    @allure.description('При создании заказа авторизованным  пользователем не передаются ингредиенты с неверным хешем')
    def test_create_order_authorized_user_bad_ingredients_hash_error(self):
        user = {'email': create_email_user_random(),
                'password': create_user_pass_random(),
                'name': create_user_name_random()
                }
        requests.post(Data.login_user, data=user)
        response = requests.post(Data.create_order, data=BurgerIngredients.non_existent_burger)
        assert response.status_code == 500 and "Internal Server Error" in response.text