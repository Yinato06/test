immutable_var = 1, 1.2, 'string'
print(immutable_var)
# immutable_var[0] = 12 (Изменить значение элементов кортежа нельзя, чтобы значения не изменились случайным образом)
mutable_list = [1,1.2,'string']
mutable_list[0] = 5
print(mutable_list)
