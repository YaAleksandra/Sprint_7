import allure
from helpers.endpoints import (create_courier)
from test_data.courier_data import CourierData, ExpectedResponses

class TestCreateCourier:
    @allure.title('Создание курьера')
    def test_create_courier_true(self):
        payload = CourierData.get_valid_courier_data()
        
        with allure.step('Отправить запрос на создание курьера'):
            response = create_courier(payload)
        
        assert response.status_code == ExpectedResponses.STATUS_CREATED
        assert response.json() == ExpectedResponses.CREATION_SUCCESS
    
    @allure.title('Нельзя создать двух одинаковых курьеров')
    def test_duplicate_courier_create_error(self):
        payload = CourierData.get_valid_courier_data()
        
        with allure.step('Создать первого курьера'):
            create_courier(payload)
        
        with allure.step('Попытаться создать второго курьера с теми же данными'):
            response = create_courier(payload)
        
        assert response.status_code == ExpectedResponses.STATUS_CONFLICT
        assert ExpectedResponses.DUPLICATE_ERROR_MSG in response.text
    
    @allure.title('Нельзя создать курьера без логина')
    def test_create_courier_without_login(self):
        payload = CourierData.get_courier_without_login()
        
        with allure.step('Отправить запрос на создание курьера без логина'):
            response = create_courier(payload)
        
        assert response.status_code == ExpectedResponses.STATUS_BAD_REQUEST
        assert ExpectedResponses.INSUFFICIENT_DATA_MSG in response.text
    
    @allure.title('Нельзя создать курьера без пароля')
    def test_create_courier_without_pass(self):
        payload = CourierData.get_courier_without_password()
        
        with allure.step('Отправить запрос на создание курьера без пароля'):
            response = create_courier(payload)
        
        assert response.status_code == ExpectedResponses.STATUS_BAD_REQUEST
        assert ExpectedResponses.INSUFFICIENT_DATA_MSG in response.text