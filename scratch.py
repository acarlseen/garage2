def print_one():
    print('one')
    
def print_two():
    print('TWO')
    
def print_three():
    print("III")
    
function_dict = {1: print_one, 2: print_two, 3:print_three}


function_dict[1]()

some_string = '100000'

print(some_string.lower())

my_dict = {'a': 1, 'b': 2, 'c':3}

x, y, z = my_dict.values()
print(x * -1)