class Data:
    base_Url = "stellarburgers.nomoreparties.site"
    main_page = f"https://{base_Url}/"
    create_user = f"https://{base_Url}/api/auth/register"
    login_user = f"https://{base_Url}/api/auth/login"
    change_user_data = f"https://{base_Url}/api/auth/user"
    create_order = f"https://{base_Url}/api/orders"
    orders_from_user = f"https://{base_Url}/api/orders"


class UserData:
    name = 'Andrey'
    email = "andreytestovich2@ya.ru"
    password = 'qqAAqq12345'
    incorrect_password = 'incpass'
    incorrect_login = 'incmail@ya.ru'


class BurgerIngredients:
    burger_existing = {'ingredients': ['61c0c5a71d1f82001bdaaa6d', '61c0c5a71d1f82001bdaaa6f']}
    burger_existing_check = "Бессмертный флюоресцентный бургер"
    non_existent_burger = {'ingredients': ['35c0c5d1fр82001bdaaa6d', '61c0c5a71d1f82001bdaaa6f']}
    burger_empty = {'ingredients': ''}

class ResponseMessages:
    authorization_required = "You should be authorised"
    user_already_created = "User already exists"
    required_fields = "Email, password and name are required fields"
    incorrect_data = "email or password are incorrect"
