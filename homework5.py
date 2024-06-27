immutable_var=(1, 0.123, True, 'Кортеж который нельзя менять', ['Список который можно изменить', 7, False])
print(immutable_var)
print( )
immutable_var[4][0]='Потому что можно менять списки'
print('Immutable tuple: ', immutable_var)

mutable_list=[1, 'kit', 0.79]
mutable_list[0]=mutable_list[0]+7
print('Mutable list: ',mutable_list)
