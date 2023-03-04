# https://www.codewars.com/kata/55332880e679dd9cb3000081
def bocce_score(balls):
    *t_b, jack = balls

    score = [0, 0]
    r_dist = []
    b_dist = []
    for el in t_b:
        if el['type'] == 'black':
            b_dist.append(((jack['distance'][0] - el['distance'][0]) ** 2 + (
                        jack['distance'][1] - el['distance'][1]) ** 2) ** 0.5)
        else:
            r_dist.append(((jack['distance'][0] - el['distance'][0]) ** 2 + (
                        jack['distance'][1] - el['distance'][1]) ** 2) ** 0.5)

    for eli in b_dist:
        flag = True
        for elj in r_dist:
            if eli > elj or eli == elj:
                flag = False
        if flag == True:
            score[0] += 1

    for eli in r_dist:
        flag = True
        for elj in b_dist:
            if eli > elj or eli == elj:
                flag = False
        if flag == True:
            score[1] += 1

    if score[0] > score[1]:
        return f'black scores {score[0] - score[1]}'
    elif score[1] > score[0]:
        return f'red scores {score[1] - score[0]}'
    else:
        return 'No points scored'

if __name__ == '__main__':
    # print(sequence_sum(2, 6, 2))
    # print(sequence_sum(20, 673388797, 5))
    ls1 = [1, 2, 3, 3]
    ls2 = [2, 3]
    diff = list(set(ls1) - set(ls2))
    print(diff)
