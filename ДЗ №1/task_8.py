# https://www.codewars.com//kata/55a3cb91d1c9ecaa2900001b
import math
def strong_enough( earthquake, age ):
    return 'Safe!' if sum(earthquake[0])*sum(earthquake[1])*sum(earthquake[2]) < 1000 * math.e**(-age/100) else 'Needs Reinforcement!'

if __name__ == '__main__':
    print(strong_enough([[5,8,7],[3,3,1],[4,1,2]], 2))
