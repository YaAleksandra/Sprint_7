import requests
import pytest
import allure
from Urls import BASE_URL
from test_data.order_data import OrderData, ExpectedOrderResponses


class TestOrderCreate:
    @allure.title('Создание заказа с разными цветами')
    @pytest.mark.parametrize('color', OrderData.get_color_variants())
    def test_create_order_with_different_color(self, color):
        payload = OrderData.get_order_with_color(color)
        
        with allure.step('Отправить запрос на создание заказа'):
            response = requests.post(f'{BASE_URL}/orders', json=payload)
        
        assert response.status_code == ExpectedOrderResponses.STATUS_CREATED
        assert ExpectedOrderResponses.TRACK_FIELD in response.json()
