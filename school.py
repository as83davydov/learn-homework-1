# school

school = [
		{'school_class': '4a', 'scores': [3, 4, 4, 5, 2]},
		{'school_class': '5a', 'scores': [3, 4, 4, 5, 2, 5, 5]},
		{'school_class': '10a', 'scores': [2, 2, 3, 4, 4, 5, 2]}
]

s = (school[0]['scores']) #класс 4а
p = (school[1]['scores']) #класс 5а
v = (school[2]['scores']) #класс 10а

score_sum_s = 0
for score in s:
    score_sum_s += score
    
score_s = score_sum_s / len(s)
print(f"Средняя оценка класса 4а: {score_s}")

score_sum_p = 0
for score in p:
    score_sum_p += score
    
score_p = score_sum_p / len(p)
print(f"Средняя оценка класса 5а: {score_p}")


score_sum_v = 0
for score in v:
    score_sum_v += score
    
score_v = score_sum_v / len(v)
print(f"Средняя оценка класса 10а: {score_v}")

score_all = (int(score_s)+int(score_p)+int(score_v))/ len(school)
print(f'Средня оценка по школе: {int(score_all)}')


