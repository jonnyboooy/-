# https://www.codewars.com/kata/52b7ed099cdc285c300001cd
def sum_of_intervals(intervals):
    arr = sorted(intervals)
    n = 0

    while n != len(arr)-1:
        if arr[n][1] >= arr[n+1][0]:
            arr[n] = (min(arr[n][0], arr[n+1][0]), max(arr[n][1], arr[n+1][1]))
            arr.remove(arr[n+1])
        else:
            n += 1
    return sum(el[1]-el[0] for el in arr)

if __name__ == '__main__':
    print(sum_of_intervals([(1, 4), (7, 10), (3, 5)]))
    print(sum_of_intervals([(0, 20), (-100_000_000, 10), (30, 40)]))