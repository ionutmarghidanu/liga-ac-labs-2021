from collections import defaultdict


def count_integers(list_1):
    result = {}
    for el in list_1:
        if el.isnumeric():
            if el in result.keys():
                result[el] += 1
            else:
                result[el] = 1

    return result


def count_order(list_1):
    result = defaultdict(int)

    for el in list_1:
        try:
            result[int(el)] += 1
        except ValueError:
            continue
    return result


if __name__ == "__main__":
    str1 = "We are having 3 numbers of 5 pieces and each of them are having 3 stars"
    list_words = str1.split(" ")
    print(count_integers(list_words))
    print(count_order(list_words))
