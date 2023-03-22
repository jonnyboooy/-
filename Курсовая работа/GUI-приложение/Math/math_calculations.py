from Data.aircraft_and_air_defense_classes import Aircraft, AirDefense
from random import randint
import matplotlib.pyplot as plt
import math

class MathCalculations:
    '''Класс MathCalculations предназначен для выполнения математических вычислений'''

    def __new__(cls, *args, **kwargs):
        return super().__new__(cls)

    def __init__(self, other, lst):
        self.aircraft = other
        self.__air_defense_list = lst
        self.figure, self.axes = plt.subplots()

    @property
    def air_defense_list(self):
        return self.__air_defense_list

    def start_end_distance(self):
        return ((self.aircraft.x_end-self.aircraft.x0)**2 + (self.aircraft.y_end-self.aircraft.y0)**2)**0.5

    def intersection(self, a, b, c):
        dis_form = b * b - 4 * a * c
        sqrt_val = math.sqrt(abs(dis_form))

        if dis_form > 0:
            print(" real and different roots ")
            print((-b + sqrt_val) / (2 * a))
            print((-b - sqrt_val) / (2 * a))

        elif dis_form == 0:
            print(" real and same roots")
            print(-b / (2 * a))

        else:
            print("Complex Roots")
            print(- b / (2 * a), " + i", sqrt_val)
            print(- b / (2 * a), " - i", sqrt_val)

    def aircraft_plot(self):
        self.axes.plot(self.aircraft.x0, self.aircraft.y0, '-k.')
        self.axes.plot(self.aircraft.x_end, self.aircraft.y_end, '-k.')

    def air_defense_plot(self):
        for el in self.air_defense_list:
            self.axes.add_patch(plt.Circle((el.x_target, el.y_target), el.r_target, fill=False))
            self.axes.plot([el.x_target], [el.y_target], '-k.')

    def show_plot(self):
        plt.grid()
        plt.show()


if __name__ == '__main__':
    mc = MathCalculations(Aircraft(x0=0,
                                   y0=0,
                                   x_end=10,
                                   y_end=7),
                          [AirDefense(x_target=5,
                                      y_target=4,
                                      r_target=5)

                           for i in range(0, 1)
                           ])

    mc.intersection(3*2/49, -21*3/7, 16)

    mc.aircraft_plot()
    mc.air_defense_plot()
    mc.show_plot()
