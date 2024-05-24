class ProUserName(Exception):
    def __init__(self, message, extra_info):
        self.message = message
        self.extra_info = extra_info


def UserName():
    person_name = str(input('Напишите своё имя: '))
    if person_name == 'Каха':
        raise ProUserName('Полюби людей', person_name)
    print(f'Привет, {person_name}')


try:
    UserName()
    print('Всё отлично получилось')
except ProUserName as exc:
    print('Припёрся КАХА')
    print(f'Сообщение об ошибке: {exc.message}')
    print(f'Дополнительная информация: Введено имя {exc.extra_info}')
else:
    a = 5
    b = 20
    print((a * b), '%')
finally:
    print('УРА!')

