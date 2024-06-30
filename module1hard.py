students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]

g_a=(grades [0])
hard_a=sum(g_a)/len(g_a)# 'считает ср. арифм.
g_b=(grades [1])
hard_b=sum(g_b)/len(g_b)# 'считает ср. арифм.
g_j=(grades [2])
hard_j=sum(g_j)/len(g_j)# 'считает ср. арифм.
g_k=(grades [3])
hard_k=sum(g_k)/len(g_k)# 'считает ср. арифм.
g_s=(grades [4])
hard_s=sum(g_s)/len(g_s)# 'считает ср. арифм.

students=tuple(students)
ter=sorted(students) #сортировка по алфавиту

Ball={ter[0]:hard_a, ter[1]:hard_b, ter[2]:hard_j, ter[3]:hard_k, ter[4]:hard_s}
print(Ball.items())

