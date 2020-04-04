"""
Given a 32-bit signed integer, reverse digits of an integer.

Example 1:

Input: 123
Output: 321
Example 2:

Input: -123
Output: -321
Example 3:

Input: 120
Output: 21
"""


class ReverseInteger(object):

    def reverse_integer(x):
        str_list = []
        for c in str(x):
            str_list.append(c)
        p = ""
        if x == 0:
            return 0
        elif x > 0:
            for i in range(int(len(str_list) / 2)):
                swap(str_list, i, len(str_list) - i - 1)

            for xx in str_list:
                p = p + xx
            return int(p)
        elif x < 0:
            for i in range(int(len(str_list) / 2) + 1):
                swap(str_list, i, len(str_list) - i - 1)
            str_list = str_list[:-1]

            for xx in str_list:
                p = p + xx
            return -int(p)


def swap(arr, start, end):
    tmp = arr[start]
    arr[start] = arr[end]
    arr[end] = tmp
    return arr


x = -2147483648
y = ReverseInteger.reverse_integer(x)
print(y)
# ===========
