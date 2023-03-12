# https://www.codewars.com/kata/517abf86da9663f1d2000003/train/python
import re

def to_camel_case(text):
    if text == '':
        return ''

    new_list = re.split('-|_', text)

    return new_list[0] + ''.join([(el[0].upper() + el[1:]) for el in new_list[1:]])

if __name__ == '__main__':
    print(to_camel_case('the-stealth-warrior'))
    