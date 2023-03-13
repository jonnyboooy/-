# https://www.codewars.com/kata/55467aaf72494e3bdc00007f/train/python
def is_rotation(s1, s2):
    if len(s1) != len(s2):
        return False

    list1 = list(s1)

    if len(list1) == 0:
        return True

    for i in list1:
        for j in range(len(list1) - 1):
            buff = list1[j]
            list1[j] = list1[j + 1]
            list1[j + 1] = buff

        if ''.join(list1) == s2:
            return True

    return False