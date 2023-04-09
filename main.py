from common.get_methods import GetMethods
from common.post_methods import PostMethods
from common.put_methods import PutMethods


# Тестовый ЛК
HEAD_URL = 'http://corp-client.taxi.tst.yandex.ru/api'
TOKEN = ''

# Продовый ЛК
# HEAD_URL = 'https://b2b-api.go.yandex.ru'
# TOKEN = ''

get_req = GetMethods(HEAD_URL, TOKEN)
post_req = PostMethods(HEAD_URL, TOKEN)
put_req = PutMethods(HEAD_URL, TOKEN)

# Обновить токен
# print(get_req.refresh_token())


# Здесь достаются нужные id
# user_id = get_req.get_users_list()["items"][0]["id"]
# department_id = get_req.get_departments_list()["items"][0]["id"]
# order_id = get_req.get_orders_list()["items"][0]["id"]

# print(get_req.get_users_list())
# print(get_req.get_user_info(user_id))
# print(get_req.get_departments_list())
# print(get_req.get_cost_centers_list())
# print(get_req.get_limits_list())
# print(get_req.get_orders_list())                  # пока ручка 2.0 не работает для тестовой среды (на проде ОК)
# print(get_req.get_active_orders_list())           # пока ручка 2.0 не работает для тестовой среды (на проде ОК)
# print(get_req.get_order_info())                   # пока ручка 2.0 не работает для тестовой среды (на проде ОК)
# print(get_req.get_order_progress())               # пока ручка 2.0 не работает для тестовой среды (на проде ОК)
# print(get_req.get_operation_tanker())
# print(get_req.get_zoneinfo(55.753711, 37.535439))

# print(post_req.create_user())
# print(post_req.archive_user(user_id))             # пока ручка 2.0 не работает для тестовой среды (на проде ОК)
# print(post_req.create_department())
# print(post_req.routestats())                      # пока ручка 2.0 не работает для тестовой среды (на проде ОК)
# print(post_req.create_order())                    # нет возможности проверить заказ без оффера (на проде должно ОК)
# print(post_req.cancel_order(order_id))            # нет возможности проверить заказ без оффера (на проде должно ОК)
# print(post_req.change_destination(order_id))      # нет возможности проверить заказ без оффера (на проде должно ОК)
# print(post_req.post_feedback(order_id))           # нет возможности проверить заказ без оффера (на проде должно ОК)

# print(put_req.update_user(user_id))               # пока ручка 2.0 не работает для тестовой среды (на проде ОК)
# print(put_req.update_department(department_id))   # Прод отдает "No method in config". В тесте не работает
# print(put_req.update_limit(user_id))              # Не проверял
