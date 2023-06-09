# Напишите 5 тестов на функцию all_division. Обязательно должен быть тест деления на ноль.
# Промаркируйте часть тестов. Например, smoke.
# В консоли с помощью pytest сделайте вызов:
# 1) Всех тестов
# 2) Только с маркером smoke
# 3) По маске. Выберите такую маску, чтобы под неё подпадали не все тесты, но больше одного
# Пришлите на проверку файл с тестами и скрины с вызовами и их результаты

import pytest


def all_division(*arg1):

    division = arg1[0]
    for i in arg1[1:]:
        division /= i
    return division

#task_3
# Из набора тестов задания task_2 создайте один тест с параметрами, используя @pytest.mark.parametrize
# Промаркируйте 1 параметр из выборки как smokе, а 1 набор данных скипните

@pytest.mark.parametrize('a, b, result', [
        pytest.param(1, 1, 1, marks=pytest.mark.skip('Не проверяем')),
        pytest.param(2, 2, 1),
        ], ids=['skip', 'smoke'])


@pytest.mark.smoke
def test_one_args():
    assert all_division(1) == 1

def test_ok():
    assert all_division(4, 2) == 2

def test_float_ok():
    assert all_division(3, 2) == 1.5

def test_three_args():
    assert all_division(9, 3, 2) == 1.5

def test_zero():
    with pytest.raises(ZeroDivisionError):
        assert all_division(3, 0)





