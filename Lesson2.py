"""
1. Создать список и заполнить его элементами различных типов данных. Реализовать скрипт проверки типа данных каждого
элемента. Использовать функцию type() для проверки типа. Элементы списка можно не запрашивать у пользователя,
а указать явно, в программе.
"""

# my_list = [2, 'text', 456, 45.3, [1, 2, 3], None, True]
# print(my_list)
# print(list(map(type, my_list)))

"""
2. Для списка реализовать обмен значений соседних элементов, т.е. Значениями обмениваются элементы с индексами
0 и 1, 2 и 3 и т.д. При нечетном количестве элементов последний сохранить на своем месте. Для заполнения списка
элементов необходимо использовать функцию input().
"""

# list2 = []  # заводим пустой список
# n = int(input("Введите количество элементов списка: "))  # задаём количество элемент в списке
# # второй вариатн через while, как на уроке (1:28)
# for i in range(n):
#     list2.append(input())
# print("Исходный список: ", list2)
# i = 1
# while i < len(list2):
#     list2[i], list2[i-1] = list2[i-1], list2[i]
#     # print(list2)
#     i += 2
# print("Итоговый список: ", list2)

"""
3. Пользователь вводит месяц в виде целого числа от 1 до 12. Сообщить к какому времени года относится месяц
(зима, весна, лето, осень). Напишите решения через list и через dict.
"""
# # Решение через list
# # Разбиваем год по временам года в виде списков
# li_winter = [1, 2, 12]
# li_spring = [3, 4, 5]
# li_summer = [6, 7, 8]
# li_autumn = [9, 10, 11]
# a = int(input("Введите номер месяца от 1 до 12: "))
# if a in li_winter:
#     print("Это зима")
# elif a in li_spring:
#     print("Это весна")
# elif a in li_summer:
#     print("Это лето")
# elif a in li_autumn:
#     print("Это осень")
# else:
#     print("Введите число от 1 до 12!")
#
# # Решение через dict
# d_winter = {"jan": 1, "feb": 2, "dec": 12}
# d_spring = {"mar": 3, "apr": 4, "may": 5}
# d_summer = {"jun": 6, "jul": 7,"aug": 8}
# d_autumn = {"sep": 9, "oct": 10,"nov": 11}
# num = int(input("Введите номер месяца от 1 до 12: "))
# for el in d_winter:
#     if num == d_winter[el]:
#         print("Это зима")
# for el in d_spring:
#     if num == d_spring[el]:
#         print("Это весна")
# for el in d_summer:
#     if num == d_summer[el]:
#         print("Это лето")
# for el in d_autumn:
#     if num == d_autumn[el]:
#         print("Это осень")
# else:
#     print("Введите число от 1 до 12!")

"""
4. Пользователь вводит строку из нескольких слов, разделённых пробелами. Вывести каждое слово с новой строки.
Строки необходимо пронумеровать. Если в слово длинное, выводить только первые 10 букв в слове.
"""

# s = input('Введите строку из нескольких слов, разделённых пробелами: ')
# li_3 = s.split(' ')
# for i, v in enumerate(li_3, 1):
#     print(i, v[:10])  # ограничиваем длину выводимых слов с помощью среза

"""
5. Реализовать структуру «Рейтинг», представляющую собой не возрастающий набор натуральных чисел.
У пользователя необходимо запрашивать новый элемент рейтинга. Если в рейтинге существуют элементы с одинаковыми
значениями, то новый элемент с тем же значением должен разместиться после них.
Подсказка. Например, набор натуральных чисел: 7, 5, 3, 3, 2.
Пользователь ввел число 3. Результат: 7, 5, 3, 3, 3, 2.
Пользователь ввел число 8. Результат: 8, 7, 5, 3, 3, 2.
Пользователь ввел число 1. Результат: 7, 5, 3, 3, 2, 1.
Набор натуральных чисел можно задать непосредственно в коде, например, my_list = [7, 5, 3, 3, 2].
"""

# my_list = [7, 5, 3, 3, 2]
# print(f'Исходный рейтинг - {my_list}')
# new_el = int(input('Введите новый элемент или 888 для выхода: '))
# while new_el != 888:
#     for el in range(len(my_list)):
#         if my_list[el] == new_el:
#             my_list.insert(el + 1, new_el)
#             break
#         elif new_el > my_list[0]:
#             my_list.insert(0, new_el)
#         elif new_el < my_list[-1]:
#             my_list.append(new_el)
#         elif my_list[el] > new_el > my_list[el + 1]:
#             my_list.insert(el + 1, new_el)
#     print(f'Текущий рейтинг - {my_list}')
#     new_el = int(input('Введите новый элемент или 888 для выхода: '))

"""
6. * Реализовать структуру данных «Товары». Она должна представлять собой список кортежей. Каждый кортеж хранит
информацию об отдельном товаре. В кортеже должно быть два элемента — номер товара и словарь с параметрами
(характеристиками товара: название, цена, количество, единица измерения). Структуру нужно сформировать программно,
т.е. запрашивать все данные у пользователя.
Пример готовой структуры:
[
(1, {“название”: “компьютер”, “цена”: 20000, “количество”: 5, “eд”: “шт.”}),
(2, {“название”: “принтер”, “цена”: 6000, “количество”: 2, “eд”: “шт.”}),
(3, {“название”: “сканер”, “цена”: 2000, “количество”: 7, “eд”: “шт.”})
]
Необходимо собрать аналитику о товарах. Реализовать словарь, в котором каждый ключ — характеристика товара,
например название, а значение — список значений-характеристик, например список названий товаров.
Пример:
{
“название”: [“компьютер”, “принтер”, “сканер”],
“цена”: [20000, 6000, 2000],
“количество”: [5, 2, 7],
“ед”: [“шт.”]
}
"""

# goods = []
# goods_feat = {'название': '', 'цена': '', 'количество': '', 'ед.': ''}
# analytics = {'название': [], 'цена': [], 'количество': [], 'ед.': []}
# num = 0
# goods_feat_ = None
# control = None
# while True:
#     control = input('Для выхода введите "Q", для продолжения "Enter", для вывода аналитики введите "A"').upper()
#     if control == 'Q':
#         break
#     num += 1
#     if control == 'A':
#         print(f'\n Аналитика: \n')
#         for k, v in analytics.items():
#             print(f'{k} : {v} \n')
#     for f in goods_feat.keys():
#         goods_feat_ = input(f'Введите "{f}":')
#         goods_feat[f] = int(goods_feat_) if (f == 'price' or f == 'quantity') else goods_feat_
#         analytics[f].append(goods_feat[f])
#     goods.append((num, goods_feat))
# print(f'\n Структура товаров:', *goods, sep='\n')
