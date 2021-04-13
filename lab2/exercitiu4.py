def flatten(list_1, depth):
    new_list = []
    while depth != 0:
        for el in list_1:
            if type(el) == list:
                new_list += el
            else:
                new_list += [el]
        depth -= 1
    return new_list


print(flatten([1, 2, [3, [4]]], 1))
