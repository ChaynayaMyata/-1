
My_dict={'Tat':2011, 'Iva':2005}
print(My_dict['Tat'])
My_dict['Ann']=2007
print(My_dict['Ann'])
My_dict.update({'Nik':2009, 'Zen':2010})
print(My_dict.pop('Tat'))
print(My_dict)

print( )
print( )

my_set={7, 79, 97 , 'Rom', 'ROM', (1,2,3), 7, 'Rom', True}
print(my_set)
my_set.add(8)
my_set2={3546, 'ok', False}
my_set=my_set.union(my_set2)
my_set.discard(97)
print(my_set)