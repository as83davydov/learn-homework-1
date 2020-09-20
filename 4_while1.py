"""

Домашнее задание №1

Цикл while: hello_user

* Напишите функцию hello_user(), которая с помощью функции input() спрашивает 
  пользователя “Как дела?”, пока он не ответит “Хорошо”
   
"""


def greeting():
    while True:
        hello_user = input('Как дела?: ')
        if hello_user == 'Хорошо':
            print('Супер')
            break
        else:
            print('А почему {}?'.format(hello_user))

    
if __name__ == "__main__":
  check_def = greeting()
  print(check_def)
