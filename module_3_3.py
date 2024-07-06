def print_params(a = 1, b = 'string', c = True):
    print(a, b, c)

print_params(b = 212, c = 'kjhi')
print_params()
print_params(b = 25)
print_params(c = [1,2,3])

values_list = [9, 'asd', False]
values_dict = {'a': 765, 'b': 43, 'c': 8978}
print_params(*values_list)
print_params(**values_dict)
values_list_2 = [1.1, 'erm']
print_params(*values_list_2, 42)
