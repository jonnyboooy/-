# https://www.codewars.com/kata/55467aaf72494e3bdc00007f/train/python
def is_rotation(s1, s2):
    if len(s1) != len(s2):
        return False

    list1 = list(s1)
    count = 0
    l1 = 0
    l2 = 0

    if len(list1) == 0:
        return True

    while count != len(list1):
        while l1 != len(list1) - 1:
            buff = list1[l1]
            list1[l1] = list1[l1 + 1]
            list1[l1 + 1] = buff
            l1 += 1

        equal = 0

        while l2 != len(list1):
            if list1[l2] == s2[l2]:
                equal += 1

            l2 += 1

        if equal == len(s2):
            return True

        count += 1
        l1 = 0
        l2 = 0

    return False

if __name__ == '__main__':
    print(is_rotation('hello','ohell'))
