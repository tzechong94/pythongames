import my_module

# print(my_module.test_var)

# my_module.test_function(123)

# test = my_module.Test()
# test.do_something()

print(__name__) # prints the imported library first

if __name__ == '__main__':
    print('The main file')