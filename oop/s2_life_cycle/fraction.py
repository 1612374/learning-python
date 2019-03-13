import math


class Fraction:

    num_fraction = 0   # static (class) variable for counting number of fraction instances

    def __init__(self, num, deno):
        self.__num = num
        self.__deno = deno
        Fraction.num_fraction += 1

    def __repr__(self):
        return "{} / {}".format(self.__num, self.__deno)

    @classmethod  # for using constructor
    def from_string(cls, fraction_str):
        num, deno = list(map(int, fraction_str.split('/')))
        return cls(num, deno)

    @staticmethod  # relevant (to the class) fucntion
    def f_gcd(a, b):
        while b:
            a, b = b, a % b

        return a

    def simplify(self):
        g = Fraction.f_gcd(self.__num, self.__deno)
        self.__num = int(self.__num / g)
        self.__deno = int(self.__deno / g)
