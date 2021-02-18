from typing import Union

import pytest


class Rational:
    def __init__(self, nominator: int, denominator: int):
        if denominator == 0:
            raise ValueError("Denominator cannot be equal to zero")
        self.nominator = nominator
        self.denominator = denominator

    def __repr__(self):
        return "Rational(" + str(self.nominator) + ", " + str(self.denominator) + ")"

    def __str__(self):
        return str(self.nominator)+"/"+str(self.denominator)

    def __add__(self, other: Union[int, float, "Rational"]):
        if isinstance(other, int):
            return self._add_int(other)
        if isinstance(other, float):
            return self._add_float(other)
        if isinstance(other, Rational):
            return self._add_rational(other)
        return NotImplemented

    def _gcd(self, other):
        a = self.denominator
        while a != 0:
            a, other = other % a, a
        return other

    def _lcm(self, other):
        return abs(other*self.denominator/self._gcd(other))

    def _add_rational(self, other: "Rational"):
        lcm = self._lcm(other.denominator)
        new_nominator = lcm/self.denominator*self.nominator + lcm/other.denominator*other.nominator
        if new_nominator != 0:
            return Rational(int(new_nominator), int(lcm))
        else:
            return 0

    def _add_float(self, other: float) -> float:
        return self.nominator/self.denominator + other

    def _add_int(self, other: int) -> "Rational":
        return Rational(int(other*self.denominator+self.nominator), self.denominator)


if __name__ == "__main__":
    rational = Rational(2, 3)
    print(type(rational.__add__(5)))
    print(rational.__str__())
