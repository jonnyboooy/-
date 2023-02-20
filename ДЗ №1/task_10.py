# https://www.codewars.com//kata/559d7951ce5e0da654000073
def alternate_sq_sum(arr):
    return (sum(pow(arr[i], 2) if i%2 != 0 else 0 for i in range(len(arr))) + sum(arr[i] if i%2 == 0 else 0 for i in range(len(arr))))

if __name__ == '__main__':
    print(alternate_sq_sum([11, 12, 13, 14, 15]))
