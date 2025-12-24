from helpers.generator import (
    generate_login,
    generate_password,
    generate_first_name
)


class CourierData:
    # Генерация тестовых данных
    @staticmethod
    def get_valid_courier_data():
        return {
            'login': generate_login(),
            'password': generate_password(),
            'first_name': generate_first_name()
        }
    
    @staticmethod
    def get_courier_without_login():
        return {
            'password': generate_password(),
            'first_name': generate_first_name()
        }
    
    @staticmethod
    def get_courier_without_password():
        return {
            'login': generate_login(),
            'first_name': generate_first_name()
        }
    
    @staticmethod
    def get_login_data(login, password):
        return {
            'login': login,
            'password': password
        }
    
    @staticmethod
    def get_wrong_password():
        return 'qwerty'
    
    @staticmethod
    def get_nonexistent_user():
        return {
            'login': 'qwerty',
            'password': '123456'
        }
    
    @staticmethod
    def get_login_without_credentials():
        return {'password': '123'}


class ExpectedResponses:
    # Ожидаемые ответы для создания курьера
    CREATION_SUCCESS = {'ok': True}
    
    # Сообщения об ошибках
    DUPLICATE_ERROR_MSG = 'Этот логин уже используется'
    INSUFFICIENT_DATA_MSG = 'Недостаточно данных для создания учетной записи'
    LOGIN_INSUFFICIENT_DATA_MSG = 'Недостаточно данных для входа'
    ACCOUNT_NOT_FOUND_MSG = 'Учетная запись не найдена'
    
    # Статус коды
    STATUS_CREATED = 201
    STATUS_BAD_REQUEST = 400
    STATUS_CONFLICT = 409
    STATUS_OK = 200
    STATUS_NOT_FOUND = 404