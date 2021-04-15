class MyClass(object):

    def __new__(cls, *args, **kwargs):
        print("Creating an instance")
        return super().__new__(cls, *args, **kwargs)

    def __init__(self):
        print('Init an instance')


my_obj = MyClass()