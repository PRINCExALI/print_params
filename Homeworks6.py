def print_params(a=1, b='строка', c=True):
    print(a, b, c)


print_params()
print_params(a=30, b='hello')
print_params(a=5, b='python', c=False)
print_params(b=25)         # работает,но пучарм ругается что
print_params(c=[1, 2, 3])  # ожидался другой тип данных(тот что был изначально)
print()
values_list = [5, 'hello', True]
values_dict = {'a': 3, 'b': 'world', 'c': False}
print_params(*values_list)
print_params(**values_dict)
values_list_2 = [7, True]
print_params(*values_list_2, 42)  # работает
