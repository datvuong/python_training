from decimal import Decimal

class Fraction:
    def __init__(self, nr, dr):
        self._nr = Decimal(str(nr))
        self.dr = Decimal(str(dr))
        self.reduce()
    
    @property
    def nr(self):
        return self._nr

    @property
    def dr(self):
        return self._dr
    
    @dr.setter
    def dr(self, new_df):
        if new_df < 0:
            self._nr = - self._nr
            self._dr = - new_df
        else:
            self._dr = new_df
    
    def __repr__(self):
        if self.dr == 0:
            raise ZeroDivisionError("Division by Zero")
        elif self.nr == 0:
            return '0'
        elif self.dr == 1:
            return f'{int(self.nr)}'
        else:
            return f'{int(self.nr)}/{int(self.dr)}'

    def __add__(self, other):
        if isinstance(other, Fraction):
            return Fraction(self.nr * other.dr + other.nr * self.dr, self.dr * other.dr)
        if isinstance(other, int):
            return Fraction(self.nr + other * self.dr, self.dr)
        if isinstance(other, float):
            return Fraction(self.nr + other * self.dr, self.dr)

    def __sub__(self, other):
        if isinstance(other, Fraction):
            return Fraction(self.nr * other.dr - other.nr * self.dr, self.dr * other.dr)
        if isinstance(other, int):
            return Fraction(self.nr - other * self.dr, self.dr)
        if isinstance(other, float):
            return Fraction(self.nr - other * self.dr, self.dr)

    def __mul__(self, other):
        if isinstance(other, Fraction):
            return Fraction(self.nr * other.nr, self.dr * other.dr)
        if isinstance(other, int):
            return Fraction(self.nr * other, self.dr)
        if isinstance(other, float):
            return Fraction(self.nr * other, self.dr)

    def __truediv__(self, other):
        if isinstance(other, Fraction):
            return Fraction(self.nr * other.dr, self.dr * other.nr)
        if isinstance(other, int):
            return Fraction(self.nr, self.dr * other)
        if isinstance(other, float):
            return Fraction(self.nr, self.dr * other)

    def hcf(self):
        x = abs(self.nr)
        y = abs(self.dr)
        while(y):
            x, y = y, x % y
        self._hcf = x
        return x

    def reduce(self):
        self.hcf()
        self._nr = int(self.nr / self._hcf)
        self.dr = int(self.dr / self._hcf)

if __name__ == '__main__':
    f = Fraction(1,2)
    f2 = Fraction(3,2)
    print(f, f2)
    print(f + f2)
    print(f - f2)
    print(f * f2)
    print(f / f2)
