# Работа со словарями
my_dict = {'Sasha':1993,'Alex':2003,'Artur':2001,'Anna':1983,'Alexa':2006}
print(my_dict)
print(my_dict['Alexa'])
print(my_dict.get('Petr'))
my_dict.update({'Petr':1962,'Alena':2005})
del my_dict['Sasha']
print(my_dict.get('Sasha'))
print(my_dict)
# Работа с множествами
my_set = {1,2,2,3,5,6,3,4,4}
my_set.add(8)
my_set.add(12)
my_set.remove(5)
print(my_set)