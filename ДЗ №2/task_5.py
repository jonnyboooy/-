# https://www.codewars.com/kata/54592a5052756d5c5d0009c3/train/python
def head(arr):
    head, *tail = arr
    return head

def tail(arr):
    head, *tail = arr
    return tail

def init(arr):
    *init, last = arr
    return init

def last(arr):
    *init, last = arr
    return last

if __name__ == '__main__':
    print(head([5, 1]))
    print(tail([1]))
    print(init([1, 5, 7, 9]))
    print(last([7, 2]))