import math


class Utilities(object):
    @staticmethod
    def ease_in(a, b, p):
        return a + (b-a)*p*p

    @staticmethod
    def ease_out(a, b, p):
        return a + (b-a)*(p*(2-p))

    @staticmethod
    def ease_in_out(a, b, p):
        return a + (b-a)*(-0.5*math.cos(math.pi*p) + 0.5)