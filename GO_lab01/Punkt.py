import math
from Wielokat import Wielokat
class Punkt:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def przynaleznosc_pkt_do_prostej(self, a, b):
        if self.y == a * self.x + b:
            return True
        else:
            return False

    def przynaleznosc_do_odcinka(self, punkt1x, punkt1y, punkt2x, punkt2y):
        if (self.x - punkt1x) * (punkt2y - punkt1y) == (self.y - punkt1y) * (punkt2x - punkt1x):
            if min(punkt1x, punkt2x) <= self.x <= max(punkt1x, punkt2x) and min(punkt1y, punkt2y) <= self.y <= max(punkt1y, punkt2y):
                return True
        return False

    def polozenie_pkt_wzgl_prostej(self, punkt1x, punkt1y, punkt2x, punkt2y):
        a = (punkt2y - punkt1y) / (punkt2x - punkt1x)
        b = punkt1y - a * punkt1x

        wartosc_funkcji = a * self.x + b

        if self.y > wartosc_funkcji:
            return 1  # Punkt leży po prawej stronie prostej
        elif self.y < wartosc_funkcji:
            return -1  # Punkt leży po lewej stronie prostej
        else:
            return 0  # Punkt leży na prostej

    def odbicie_wzgl_linii(self, punkt1x, punkt1y, punkt2x, punkt2y):
        if punkt1x == punkt2x:
            # Prosta jest pionowa, a równanie przyjmuje postać x = const
            x_odbicie = 2 * punkt1x - self.x
            y_odbicie = self.y
        elif punkt1y == punkt2y:
            y_odbicie = 2 * punkt1y - self.y
            x_odbicie = self.x
        else:
            a = (punkt2y - punkt1y) / (punkt2x - punkt1x)
            b = punkt1y - a * punkt1x
            # Obliczanie współrzędnych odbitego punktu
            x_odbicie = (self.x * (1 - a**2) + 2 * a * (self.y - b)) / (1 + a**2)
            y_odbicie = ((2 * a * x_odbicie - self.y + 2 * b) / (1 + a**2))
        return x_odbicie, y_odbicie

    def odl_punkt_prosta(self, a, b, c):
        licznik = abs(a * self.x + b * self.y + c)
        mianownik = math.sqrt(a ** 2 + b ** 2)
        odleglosc = licznik / mianownik

        return odleglosc


