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
  for class_dict in school:
    class_mean = get_mean(class_dict['scores'])
    class_name = class_dict['school_class']
    print(class_name, class_mean)

  school_mean = [school[0]['scores'], school[1]['scores'], school[2]['scores']]
  print(sum([x[1] for x in school_mean])/len(school_mean))
