# https://www.codewars.com/kata/517abf86da9663f1d2000003/train/python
def to_camel_case(text):
    l = 0

    result = ''

    while l != len(text):
        if text[l] not in ['-', '_']:
            result += text[l]
            l += 1
        else:
            result += text[l + 1].upper()
            l += 2

    return result

if __name__ == '__main__':
    print(to_camel_case("the-stealth-warrior"))
