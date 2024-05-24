class InvalidDataException(Exception):
    pass


def InvalidData():
    a = int(input('Укажите год рождения: '))
    if a >= 2020:
        raise InvalidDataException('Вход при достижении возраста 25 лет')
    print('Добро пожаловать')


InvalidData()
# raise сообщает об ошибке, а блок try_except перехватывает ошибку

