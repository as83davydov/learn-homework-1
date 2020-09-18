"""

Домашнее задание №1

Цикл for: Оценки

* Создать список из словарей с оценками учеников разных классов 
  школы вида [{'school_class': '4a', 'scores': [3,4,4,5,2]}, ...]
* Посчитать и вывести средний балл по всей школе.
* Посчитать и вывести средний балл по каждому классу.
"""
school = [
		{'school_class': '4a', 'scores': [3, 4, 4, 5, 2]},
		{'school_class': '5a', 'scores': [3, 4, 4, 5, 2, 5, 5]},
		{'school_class': '10a', 'scores': [2, 2, 3, 4, 4, 5, 2]}
]

def get_mean(mark_list):
    
    list_sum = 0
    for score in mark_list:
        list_sum += score
    
    score_s = list_sum / len(mark_list)
    return(score_s)
    
if __name__ == "__main__":
  mean_list = [] #способ_1

for class_dict in school:
    class_mean = get_mean(class_dict['scores'])
    class_name = class_dict['school_class']
    mean_list.append(class_mean) #способ_1
    print(f"Средняя оценка класса: {class_name} - {class_mean}")
    print(mean_list) #способ_1 выводит что лежит в списке, необязательная строка

sum_school = get_mean(mean_list) #способ_1
print(sum_school) #способ_1

global_sum = 0 #способ_2
len_sum = 0 #способ_2

for class_dict in school: #способ_2
    global_sum += sum(class_dict['scores'])
    len_sum += len(class_dict['scores'])

print(f"Средняя оценка школы: {global_sum/len_sum}") #способ_2

