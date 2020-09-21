"""

Домашнее задание №1

Условный оператор: Сравнение строк

* Написать функцию, которая принимает на вход две строки
* Проверить, является ли то, что передано функции, строками. 
  Если нет - вернуть 0
* Если строки одинаковые, вернуть 1
* Если строки разные и первая длиннее, вернуть 2
* Если строки разные и вторая строка 'learn', возвращает 3
* Вызвать функцию несколько раз, передавая ей разные праметры 
  и выводя на экран результаты

"""

def in_str (first_string, second_string):
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    
    from collections import Counter
    a = first_string
    b = second_string
    if not (type(a) == str and type(b) == str):
        return '0'
    elif (Counter(a) == Counter(b)):
        return '1'
    elif len(a) > len(b):
        return '2'
    elif (Counter(a) != Counter(b) and 'learn' in b.lower()):
        return '3'
    else:
        return 'True'
        

 
if __name__ == "__main__":
    print(in_str(11, 211))
    print(in_str("abc", 'abc'))
    print(in_str('one two three', 'one two'))
    print(in_str('one', 'Learn'))
    print(in_str('11', '211'))