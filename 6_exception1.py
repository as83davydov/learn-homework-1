"""

Домашнее задание №1

Исключения: KeyboardInterrupt

* Перепишите функцию hello_user() из задания while1, чтобы она 
  перехватывала KeyboardInterrupt, писала пользователю "Пока!" 
  и завершала работу при помощи оператора break
    
"""

def greeting ():
    while True:
        try:
            hello_user = input('Как дела?: ')
        except KeyboardInterrupt:
            print('Пока')
        if hello_user == 'Хорошо':
            print('Супер')
            break
        else:
            print('А почему {}?'.format(hello_user))

if __name__ == "__main__":
    check_def = greeting()
    print (check_def)


