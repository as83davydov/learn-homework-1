"""
Создать список из десяти целых чисел.
Вывести на экран каждое число, увеличенное на 1

"""

numbers = [3, 5, 7, 9, 10, 15, 17, 20, 23, 25,]
for number in numbers:
    one_more = number + 1
    print(one_more)

"""
Ввести с клавиатуры строку.
Вывести эту же строку вертикально: по одному символу на строку консоли.

"""

#variant1
in_list = input('Введите c клавиатуры строку: ')
list_save = str(in_list)
for string1 in list_save.split(): #разобьет по словам
    print(string1)


#variant2
in_list = input('Введите c клавиатуры строку: ')
list_save = str(in_list)
# for string1 in list_save:
print("\n".join(list(list_save)))


