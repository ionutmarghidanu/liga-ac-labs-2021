class MyException(Exception):
    pass


class MyExceptionSecond(GeneratorExit):
    pass


if __name__ == '__main__':
    try:
        raise "Test string"

    except (MyException, MyExceptionSecond):
        print('Exception was caught')
