# https://www.codewars.com/kata/587a88a208236efe8500008b/train/python
def sequence_sum(begin_number, end_number, step):
    n = 1+((end_number - begin_number)//step)
    if n < 0:
        return 0
    else:
        return int(((2*begin_number)+(step*(n-1)))*n//2)

if __name__ == '__main__':
    print(sequence_sum(2, 6, 2))
    print(sequence_sum(20, 673388797, 5))
