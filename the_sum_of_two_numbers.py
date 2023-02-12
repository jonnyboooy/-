def the_sum_of_two_numbers():
    while True:
        try:
            a = float(input('Введите первое число: '))
            break
        except:
            print('\nПервое число введено некорректно!\n'
                  'Попробуйте еще раз!\n')

    while True:
        try:
            b = float(input('Введите второе число: '))
            break
        except:
            print('\nВторое число введено некорректно!\n'
                  'Попробуйте еще раз!\n')

    return float(a) + float(b)

if __name__ == '__main__':
    print(the_sum_of_two_numbers())
