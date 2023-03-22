class Aircraft():
    '''Класс Aircraft предназначен для описания экземпляра ВС'''

    def __new__(cls, *args, **kwargs):
        return super().__new__(cls)

    def __init__(self, x0, y0, x_end, y_end):
        self.__x0 = x0
        self.__y0 = y0
        self.__x_end = x_end
        self.__y_end = y_end

    @property
    def x0(self):
        return self.__x0

    @property
    def y0(self):
        return self.__y0

    @property
    def x_end(self):
        return self.__x_end

    @property
    def y_end(self):
        return self.__y_end


class AirDefense():
    '''Класс AirDefense предназначен для описания экземпляра ПВО'''

    def __new__(cls, *args, **kwargs):
        return super().__new__(cls)

    def __init__(self, x_target, y_target, r_target):
        self.__x_target = x_target
        self.__y_target = y_target
        self.__r_target = r_target

    @property
    def x_target(self):
        return self.__x_target

    @property
    def y_target(self):
        return self.__y_target

    @property
    def r_target(self):
        return self.__r_target


# a = Aircraft(4, 5, 6, 7)
# print(a.x0)
