from operations.forms import *
from operations.models import *


def _order_validate(user, order, tasks): # TODO: метод проверки тасков
    return None

def _moved_quants(user, order, tasks): # TODO: метод переноса квантов
    return None


def create_order(user_id, post): #Создаем заказ
    data = post.dict()
    data['order_creator'] = user_id
    data['order_updater'] = user_id
    new_order = OrderForm(data)
    #TODO: Вставить проверку заказа
    #TODO: Вставить поиск квантов в источнике
    #TODO: Вставить проверку места назначения, блокировки
    if new_order.is_valid():
        order_saved = new_order.save()
    else:
        return {'error': new_order.errors.as_data() }
        #TODO: Добавить иключение
    s = 'task_set-'
    all_tasks = []
    for i in range(0,10000): # Заполняем строки заказа
        data_task = {}
        for field in Task._meta.get_fields():# Пробегаемся по всем полям
            data_task[field.name] = data.get(s+str(i)+'-' +field.name)
            if field.name == 'creator':
                data_task['creator'] = user_id
            if field.name == 'updater':
                 data_task['updater'] = user_id
        if data_task.get('material'):
            data_task['status'] = data.get('status') #заполняем часть из шапки заказа
            data_task['bu'] = data.get('bu')
            data_task['order'] = order_saved.pk
            new_task = TaskForm2(data_task)
            if new_task.is_valid(): #Валидируем поля по общим правилам
                all_tasks.append(new_task) # добавляем в пулл после все проверок
            else:
                return {'error': new_task.errors.as_data() }
                #TODO: Добавить удаление ордера и прислать список ошибок
        else:
            break #Прерываем цикл, что бы не ждат еще 9999 итераций
    saved_tasks = []
    #TODO: Вставить проверку задач, по маршрутам там и тд
    #confirmed = _order_validate(user_id,new_order, all_tasks) #Подтвердить маршруты
    #quants = _moved_quants(user_id, new_order, all_tasks)# Подтвердить и зарезервировать локации для размещения
    #if confirmed == True and quants == True:
    #    pass
    #else:
    #    pass # Если что то не пройдено, то удалить все
    for t in all_tasks:
        save_t = t.save()
        saved_tasks.append(save_t)

    return {'order':order_saved, 'tasks': saved_tasks}

