def divide(a, b):
    try:
        c = a / b
    except ZeroDivisionError:
        print('Zero division error raised')
    else:
        print('Value returned is: {}'.format(c))
    finally:
        print('Code is in finally')

if __name__ == '__main__':
   #divide(1, 2)
   divide(1,0)
