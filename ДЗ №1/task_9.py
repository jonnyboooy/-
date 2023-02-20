# https://www.codewars.com//kata/5a54e796b3bfa8932c0000ed
def jumping_number(number):
    for i in range(len(str(number))-1):
        if abs(int(str(number)[i])-int(str(number)[i+1])) != 1: return 'Not!!'
    return 'Jumping!!'

if __name__ == '__main__':
    print(jumping_number(32123))
