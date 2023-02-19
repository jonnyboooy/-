def ensure_question(s):
    return ''.join(s+'?' if len(s) == 0 or s[-1] != '?' else s)

if __name__ == '__main__':
    print(ensure_question('What'))
