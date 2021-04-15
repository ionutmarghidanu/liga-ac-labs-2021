def adder(*num):
    sum = 0
    print(num)
    for elem in num:
        sum = sum + elem

    return sum


print(adder(1))
print(adder(1,2))
print(adder(1,2,3))