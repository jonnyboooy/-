# https://www.codewars.com//kata/57faf12b21c84b5ba30001b0
def remove(s):
    return ''.join(el for el in s if el!= '!') + '!'

if __name__ == '__main__':
    print(remove('!H!i'))
    
