# https://www.codewars.com//kata/57a429e253ba3381850000fb
def bmi(weight, height):
    if weight/pow(height, 2) <= 18.5: return 'Underweight'
    elif weight/pow(height, 2) <= 25: return 'Normal'
    elif weight/pow(height, 2) <= 30: return 'Overweight'
    else: return 'Obese'

if __name__ == '__main__':
    print(bmi(80, 180))
