def even(list_1):
    new_list = []
    for i in range(len(list_1)):
        if list_1[i] % 2 == 0:
            new_list.append(list_1[i])
    return new_list


def even1(list_1):
    return [el for el in list_1 if el % 2 == 0]


def even_func(elem):
    return elem % 2 == 0


def even2(list_1):
    return list(filter(even_func, list_1))


def even3(list_1):
    return list(filter(lambda elem: elem % 2 == 0, list_1))


if __name__ == "__main__":
    print(even([1, 2, 3, 4]))
    print(even1([1, 2, 3, 4]))
    print(even2([1, 2, 3, 4]))
    print(even3([1, 2, 3, 4]))
