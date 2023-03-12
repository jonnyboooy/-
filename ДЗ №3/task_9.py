# https://www.codewars.com/kata/54e6533c92449cc251001667/train/python
def unique_in_order(sequence):
    if len(sequence) == 0:
        return []

    result = [sequence[0]]

    for i in range(len(sequence)):
        if sequence[i] != result[-1]:
            result.append(sequence[i])

    return result
