def remove(s):
    return ''.join(el for el in s if el!= '!') + '!'

if __name__ == '__main__':
    print(remove('!H!i!'))
    
