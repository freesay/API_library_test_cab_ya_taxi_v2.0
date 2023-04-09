from common.common import Common
from common.json_methods import load_data


class GetMethods(Common):
    def __init__(self, head_url, token):
        super().__init__(head_url, token)

    def get_users_list(self):
        """
        Метод получает список сотрудников клиента.
        """
        file_name = "users_list.json"
        postfix = f"/2.0/users"
        users_list = self.get_response(file_name, postfix)
        return users_list

    def get_user_info(self, user_id):
        """
        Метод получает детальную информацию о сотруднике.
        """
        file_name = "user_info.json"
        postfix = f"/2.0/users?user_id={user_id}"
        user_info = self.get_response(file_name, postfix)
        return user_info

    def get_departments_list(self):
        """
        Метод получает информацию о подразделениях.
        """
        file_name = "departments_list.json"
        postfix = f"/integration/2.0/departments/list"
        departments_list = self.get_response(file_name, postfix)
        return departments_list

    def get_cost_centers_list(self):
        """
        Метод получает информацию о центрах затрат.
        """
        file_name = "cost_centers_list.json"
        postfix = f"/integration/2.0/cost_centers/list"
        cost_centers_list = self.get_response(file_name, postfix)
        return cost_centers_list

    def get_limits_list(self):
        """
        Метод получает информацию о центрах затрат.
        """
        file_name = "limits_list.json"
        postfix = f"/integration/2.0/limits/search"
        limits_list = self.get_response(file_name, postfix)
        return limits_list

    def get_orders_list(self):
        """
        Метод получает информацию о последних заказах.
        """
        file_name = "orders_list.json"
        postfix = f"/integration/2.0/orders/list"
        orders_list = self.get_response(file_name, postfix)
        return orders_list

    def get_active_orders_list(self, user_id):
        """
        Метод получает информацию об активных заказах со статусами.
        """
        file_name = "active_orders_list.json"
        postfix = f"/integration/2.0/orders/active?user_id={user_id}"
        active_orders_list = self.get_response(file_name, postfix)
        return active_orders_list

    def get_order_info(self, order_id):
        """
        Метод получает информацию о конкретной поездке.
        """
        file_name = "order_info.json"
        postfix = f"/integration/2.0/orders/info?order_id={order_id}"
        order_info = self.get_response(file_name, postfix)
        return order_info

    def get_order_progress(self, order_id):
        """
        Метод позволяет узнать статус заказа и местонахождение машины.
        """
        file_name = "order_progress.json"
        postfix = f"/integration/2.0/orders/progress?order_id={order_id}"
        order_progress = self.get_response(file_name, postfix)
        return order_progress

    def get_operation_tanker(self):
        """
        Метод получает информацию об оперциях сервиса "Заправки"
        """
        file_name = "operation_tanker.json"
        postfix = '/integration/2.0/orders/tanker'
        operation_tanker = self.get_response(file_name, postfix)
        return operation_tanker

    def get_zoneinfo(self, x, y):
        """
        Метод получает информацию о зоне
        """
        file_name = "zoneinfo.json"
        postfix = f'/2.0/zoneinfo?lat={x}&lon={y}'
        zoneinfo = self.get_response(file_name, postfix)
        return zoneinfo
