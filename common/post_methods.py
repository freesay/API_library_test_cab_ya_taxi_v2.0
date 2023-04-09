from common.common import Common
from common.json_methods import load_data


class PostMethods(Common):
    def __init__(self, head_url, token):
        super().__init__(head_url, token)

    def create_user(self):
        """
        Метод создает сотрудника.
        """
        file_name = "created_user.json"
        postfix = f"/2.0/users"
        data = load_data(self.parent_dir_request, self.post_examples, 'create_user.json')
        create_user = self.post_response(file_name, postfix, data)
        return create_user

    def archive_user(self, user_id):
        """
        Метод удаляет сотрудника.
        """
        file_name = "archive_user.json"
        postfix = f"/integration/2.0/users/archive?user_id={user_id}"
        archive_user = self.post_response(file_name, postfix)
        return archive_user

    def create_department(self):
        """
        Метод создает подразделение.
        """
        file_name = "create_department.json"
        postfix = f"/2.0/departments/create"
        data = load_data(self.parent_dir_request, self.post_examples, 'create_department.json')
        create_department = self.post_response(file_name, postfix, data)
        return create_department

    def routestats(self):
        """
        Метод получает информацию о предстоящей поездке
        """
        file_name = "routestats.json"
        postfix = '/integration/2.0/orders/routestats'
        data = load_data(self.parent_dir_request, self.post_examples, 'routestats.json')
        routestats = self.post_response(file_name, postfix, data)
        return routestats

    def create_order(self):
        """
        Создать заказ.
        """
        file_name = "create_order.json"
        postfix = f"/integration/2.0/orders/create"
        data = load_data(self.parent_dir_request, self.post_examples, 'create_order.json')
        create_order = self.post_response(file_name, postfix, data)
        return create_order

    def cancel_order(self, order_id):
        """
        Отменить заказ.
        """
        file_name = "create_order.json"
        postfix = f"/integration/2.0/orders/cancel?order_id={order_id}"
        data = load_data(self.parent_dir_request, self.post_examples, 'cancel_order.json')
        cancel_order = self.post_response(file_name, postfix, data)
        return cancel_order

    def change_destination(self, order_id):
        """
        Изменить маршрут.
        """
        file_name = "change_destination.json"
        postfix = f"/integration/2.0/orders/change-destinations?order_id={order_id}"
        data = load_data(self.parent_dir_request, self.post_examples, 'change_destination.json')
        change_destination = self.post_response(file_name, postfix, data)
        return change_destination

    def post_feedback(self, order_id):
        """
        Оставить отзыв водителю.
        """
        file_name = "post_feedback.json"
        postfix = f"/integration/2.0/orders/feedback?order_id={order_id}"
        data = load_data(self.parent_dir_request, self.post_examples, 'post_feedback.json')
        post_feedback = self.post_response(file_name, postfix, data)
        return post_feedback
