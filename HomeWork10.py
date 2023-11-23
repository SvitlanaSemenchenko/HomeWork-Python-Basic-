import string
import keyword

def is_valid_variable_name(name):
    if name == '_':
        print(True)
        return
    if name[0].isalpha() and all(char.isalnum() or char == '_' for char in name[1:]):        
        if name not in keyword.kwlist:            
            if not any(char.isupper() for char in name):
                print(True)
                return
    print(False)

# Examples:
is_valid_variable_name('_')
is_valid_variable_name('x')
is_valid_variable_name('get_value')
is_valid_variable_name('get value')
is_valid_variable_name('get!value')
is_valid_variable_name('some_super_puper_value')
is_valid_variable_name('Get_value')
is_valid_variable_name('get_Value')
is_valid_variable_name('getValue')
is_valid_variable_name('3m')
is_valid_variable_name('m3')
