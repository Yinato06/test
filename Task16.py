values_list = ['string', False, 4]
values_dict = {'a': True, 'b': 'hm...', 'c': 3}
values_list_2 = [5, 'cupcake']


def print_params(a=1, b='строка', c=True):
    print(a, b, c)


print_params()
print_params(a=3)
print_params(5, 'ssss', False)
print_params(5, 'ssss', False, 3)
print_params(b=25)
print_params(c=[1, 2, 3])
print_params(*values_list)
print_params(**values_dict)
print_params(*values_list_2, 42)
