import allure
from helpers.endpoints import create_courier, login_courier
from test_data.courier_data import CourierData, ExpectedResponses


class TestLoginCourier:
    @allure.title('Успешная авторизация курьера в системе')
    def test_courier_successful_login(self):
        courier_data = CourierData.get_valid_courier_data()
        
        with allure.step('Создать курьера'):
            create_courier(courier_data)
        
        with allure.step('Авторизоваться под созданным курьером'):
            login_data = CourierData.get_login_data(
                courier_data['login'], 
                courier_data['password']
            )
            response = login_courier(login_data)
        
        assert response.status_code == ExpectedResponses.STATUS_OK
        assert 'id' in response.json()
    
    @allure.title('Ошибка авторизации при неверном пароле')
    def test_login_incorrect_pass_error(self):
        courier_data = CourierData.get_valid_courier_data()
        
        with allure.step('Создать курьера'):
            create_courier(courier_data)
        
        with allure.step('Попытаться авторизоваться с неверным паролем'):
            login_data = CourierData.get_login_data(
                courier_data['login'], 
                CourierData.get_wrong_password()
            )
            response = login_courier(login_data)
        
        assert response.status_code == ExpectedResponses.STATUS_NOT_FOUND
        assert ExpectedResponses.ACCOUNT_NOT_FOUND_MSG in response.text
    
    @allure.title('Ошибка авторизации при отсутствии логина')
    def test_login_without_login_error(self):
        with allure.step('Попытка авторизоваться без логина'):
            payload = CourierData.get_login_without_credentials()
            response = login_courier(payload)
        
        assert response.status_code == ExpectedResponses.STATUS_BAD_REQUEST
        assert ExpectedResponses.LOGIN_INSUFFICIENT_DATA_MSG in response.text
    
    @allure.title('Ошибка авторизации несуществующего пользователя')
    def test_login_nonexistent_user_error(self):
        with allure.step('Попытка авторизоваться несуществующим пользователем'):
            payload = CourierData.get_nonexistent_user()
            response = login_courier(payload)
        
        assert response.status_code == ExpectedResponses.STATUS_NOT_FOUND
