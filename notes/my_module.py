def test_function(content):
    print(f'this is an imported function with the parameter: {content}')

class Test:
    def __init__(self):
        self.name = "my app"
        self.value = 12

    def do_something(self):
        print('hello')

test_var = 'test'

## dunderman
if __name__ == '__main__':
    print(__name__)