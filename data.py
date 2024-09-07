class Data:
    base_Url = "https://stellarburgers.nomoreparties.site"
    main_page = "https://stellarburgers.nomoreparties.site/"
    create_user = "https://stellarburgers.nomoreparties.site/api/auth/register"
    login_user = "https://stellarburgers.nomoreparties.site/api/auth/login"
    change_user_data = "https://stellarburgers.nomoreparties.site/api/auth/user"
    create_order = "https://stellarburgers.nomoreparties.site/api/orders"
    orders_from_user = "https://stellarburgers.nomoreparties.site/api/orders"


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