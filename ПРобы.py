
list_2 = [2, 3, 5, 9, 23, 10]
sum_ = 0
for i in range(len(list_2)):
    sum_ += list_2[i]  # ВОПРОСИЩЕ, что за += и зачем оно???
    print(sum_)

for i in range(1, 11):  # start, stop, step здесь указано начало и конец последовательности,
    for j in range(1, 11):  # большая граница не входит в последовательность!
        print(f'{i} x {j} == {i * j}')  # ВОПРОС К ПРЕПОДАВАТЕЛЮ, что такое f и зачем оно???

dict_ = {'a': 1, 'b': 2, 'c': 3}
for i, k in dict_items():  # items - не смогла разобраться с ошибкой
    print(i, k)