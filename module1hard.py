students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]

a=0
grades [0+a]=sum(grades [0+a])/len(grades [0+a])# 'считает ср. арифм.
a=a+1
grades [0+a]=sum(grades [0+a])/len(grades [0+a])# 'считает ср. арифм.
a=a+1
grades [0+a]=sum(grades [0+a])/len(grades [0+a])# 'считает ср. арифм.
a=a+1
grades [0+a]=sum(grades [0+a])/len(grades [0+a])# 'считает ср. арифм.
a=a+1
grades [0+a]=sum(grades [0+a])/len(grades [0+a])# 'считает ср. арифм.


students=tuple(students)
students=sorted(students) #сортировка по алфавиту

print(dict(zip(students,grades)))#объединение словарей
