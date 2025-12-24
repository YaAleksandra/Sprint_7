import allure
import pytest
from helpers.endpoints import get_orders
from test_data.order_data import ExpectedOrderResponses


class TestOrderList:
    @allure.title('Получение списка заказов')
    def test_get_orders_list(self):
        with allure.step('Отправить запрос на получение списка заказов'):
            response = get_orders()
        
        assert response.status_code == ExpectedOrderResponses.STATUS_OK
        data = response.json()
        assert ExpectedOrderResponses.ORDERS_FIELD in data
        assert isinstance(data[ExpectedOrderResponses.ORDERS_FIELD], list)