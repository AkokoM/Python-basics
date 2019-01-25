# Задача-2:
# Даны два произвольные списка.
# Удалите из первого списка элементы, присутствующие во втором списке.

# list_a = ['g', 78, 'good', 'hight', 777]
# list_b = ['S', 78, 'good', 555, 'Dog']
# mergedlist = list(set(list_a + list_b))
# print(mergedlist)

from random import randint

list_1= [randint(10, 20) for i in range(10)]
list_2 = [randint(10, 25) for i in range(10)]
print('Первый список =', list_1)
print('Второй список =', list_2)
list_1 = [i for i in list_1 if i not in list_2]
print('Первый список после удаления элементов второго списка =', list_1)