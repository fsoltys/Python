from math import log


class LogPwr:
    def __init__(self, a):
        self.a = a

    def log(self, x=1):
        return log(x, self.a)

    def power(self, x=1):
        return x ** self.a


number = LogPwr(2)

print(number.log(8), number.power(2))
