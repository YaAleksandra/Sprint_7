from helpers.generator import (
    generate_first_name,
    generate_last_name,
    generate_address,
    generate_metro_st,
    generate_phone_num,
    generate_rent_time,
    generate_delivery_date,
    generate_comment
)


class OrderData:
    @staticmethod
    def get_base_order_data():
        return {
            'first_name': generate_first_name(),
            'last_name': generate_last_name(),
            'address': generate_address(),
            'metroSt': generate_metro_st(),
            'phone': generate_phone_num(),
            'rentTime': generate_rent_time(),
            'deliveryDate': generate_delivery_date(),
            'comment': generate_comment()
        }
    
    @staticmethod
    def get_order_with_color(color):
        data = OrderData.get_base_order_data()
        data['color'] = color
        return data
    
    @staticmethod
    def get_color_variants():
        return [
            ['BLACK'],
            ['GREY'],
            ['BLACK', 'GREY'],
            []
        ]


class ExpectedOrderResponses:
    STATUS_CREATED = 201
    STATUS_OK = 200
    TRACK_FIELD = 'track'
    ORDERS_FIELD = 'orders'