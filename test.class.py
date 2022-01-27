class Test:
    x = 5
    y = 6

    def __init__(self):
        x = 10
    
    def __str__(myclass):
        return 'test={ x=' + str(myclass.x) + 'y=' + str(myclass.y) + '}'

    def my_function():
        return 'X'


test = Test()

print(test)
