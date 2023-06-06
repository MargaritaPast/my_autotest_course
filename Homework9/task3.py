# Дан файл test_file/task_3.txt можно считать, что это запись покупок в магазине, где указана только цена товара
# В каждой строке файла записана цена товара.
# Покупки (т.е. несколько подряд идущих цен) разделены пустой строкой
# Нужно найти сумму трёх самых дорогих покупок, которые запишутся в переменную three_most_expensive_purchases

list_purchase = []
purchase = 0
with open('test_file/task_3.txt', 'r') as file:
    for line in file:
        if line != '\n':
            purchase = purchase + int(line)
        else:
            list_purchase.append(purchase)
            purchase = 0
list_purchase.sort(reverse=True)
three_most_expensive_purchases = sum(list_purchase[:3])

assert three_most_expensive_purchases == 202346
