# https://www.codewars.com/kata/5a55f04be6be383a50000187/train/python
def special_number(number):
    for el in str(number):
        if not 0 <= int(el) <= 5:
            return 'NOT!!'

    return 'Special!!'