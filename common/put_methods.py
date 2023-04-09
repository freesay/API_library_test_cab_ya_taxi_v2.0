from common.common import Common
from common.json_methods import load_data


class PutMethods(Common):
    def __init__(self, head_url, token):
        super().__init__(head_url, token)

    def update_user(self, user_id):
        """
        Метод изменяет данные сотрудника.
        """
        file_name = "update_user.json"
        postfix = f"/integration/2.0/users?user_id={user_id}"
        data = load_data(self.parent_dir_request, self.put_examples, 'update_user.json')
        update_user = self.put_response(file_name, postfix, data)
        return update_user

    def update_department(self, department_id):
        """
        Метод изменяет данные подразделения.
        """
        file_name = "update_department.json"
        postfix = f"/integration/2.0/departments/update/{department_id}"
        data = load_data(self.parent_dir_request, self.put_examples, 'update_department.json')
        update_department = self.put_response(file_name, postfix, data)
        return update_department

    def update_limit(self, user_id):
        """
        Метод изменяет лимит сотрудника.
        """
        file_name = "update_limit.json"
        postfix = f"/integration/2.0/limits/personal?user_id={user_id}"
        data = load_data(self.parent_dir_request, self.put_examples, 'update_limit.json')
        update_limit = self.put_response(file_name, postfix, data)
        return update_limit
