def total(first, *number, **params):
    print('first', first)

    for single in number:
        print(single)

    for param1, param2 in params.items():
        print(param1, param2)


total(10, 1, 3, 4, 5, a=1, b="ggg", c=4, d='g')
