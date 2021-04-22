class Fibonnaci:

    def __init__(self, max):
        self.max = max
        self.current = 1
        self.previous = 0

    def __next__(self):
        self.previous, self.current = self.current, self.previous + self.current
        if self.previous >= self.max:
            raise StopIteration()
        return self.current

    def __iter__(self):
        return self


def fib(max):
    a, b = 0, 1
    for i in range(max):
        yield a
        a, b = b, a + b


if __name__ == '__main__':
    # f = Fibonnaci(5)
    # for elem in f:
    #     print(elem)

    a = fib(5)
    print(next(a))
    print(next(a))
    print(next(a))
    print(next(a))
    print(next(a))
    print(next(a))
