import math
class Linia:
    def __init__(self, punkt1x, punkt1y, punkt2x, punkt2y):
        self.punkt1x = punkt1x
        self.punkt1y = punkt1y
        self.punkt2x = punkt2x
        self.punkt2y = punkt2y

    def wyznacz_rownanie_prostej(self):
        if self.punkt1x == self.punkt2x:
            a = None
            b = self.punkt1x
        else:
            a = (self.punkt2y - self.punkt1y) / (self.punkt2x - self.punkt1x)
            b = self.punkt1y - a * self.punkt1x
        return a, b

    def translacja(self, wektor):
        self.punkt1x += wektor[0]
        self.punkt1y += wektor[1]
        self.punkt2x += wektor[0]
        self.punkt2y += wektor[1]
        return self.punkt1x, self.punkt1y, self.punkt2x, self.punkt2y

    def punkt_przecięcia_dwoch_prostych(self, a1, b1, c1, a2, b2, c2):
        wyznacznik = a1 * b2 - a2 * b1

        # Sprawdzenie, czy proste są równoległe (wyznacznik równy zero)
        if wyznacznik == 0:
            print("Proste są równoległe, brak punktu przecięcia.")
            return None

        # Obliczenie współrzędnych punktu przecięcia
        x = (b1 * c2 - b2 * c1) / wyznacznik
        y = (a2 * c1 - a1 * c2) / wyznacznik
        return x, y

    def punkt_przeciecia_dwoch_prostych_b(self, p1_start, p1_end, p2_start, p2_end):
        if p1_end[0] - p1_start[0] != 0:
            a1 = (p1_end[1] - p1_start[1]) / (p1_end[0] - p1_start[0])
        else:
            a1 = None
        if a1 is not None:
            b1 = p1_start[1] - a1 * p1_start[0]
        else:
            b1 = p1_start[0]

        if p2_end[0] - p2_start[0] != 0:
            a2 = (p2_end[1] - p2_start[1]) / (p2_end[0] - p2_start[0])
        else:
            a2 = None
        if a2 is not None:
            b2 = p2_start[1] - a2 * p2_start[0]
        else:
            b2 = p2_start[0]

        # Obliczenie punktu przecięcia prostych
        if a1 is None and a2 is None:
            print("Obie linie są równoległe do osi Y, brak punktu przecięcia.")
            return None
        elif a1 is None:
            x_przeciecia = p1_start[0]
            y_przeciecia = a2 * x_przeciecia + b2
        elif a2 is None:
            x_przeciecia = p2_start[0]
            y_przeciecia = a1 * x_przeciecia + b1
        else:
            x_przeciecia = (b2 - b1) / (a1 - a2)
            y_przeciecia = a1 * x_przeciecia + b1

        return x_przeciecia, y_przeciecia

    def kat_m_liniami(self, przeciecie, p1_start, p2_start):
        u = (przeciecie[0] - p1_start[0], przeciecie[1] - p1_start[1])
        v = (przeciecie[0] - p2_start[0], przeciecie[1] - p2_start[1])

        il_sk = u[0] * v[0] + u[1] * v[1]
        u_dl = math.sqrt(u[0] ** 2 + u[1] ** 2)
        v_dl = math.sqrt(v[0] ** 2 + v[1] ** 2)

        if u_dl == 0 or v_dl == 0:
            print("Jeden z wektorów ma długość zero, nie można obliczyć kąta")
            return None

        alfa_rad = math.acos(il_sk / (u_dl * v_dl))
        alfa_st = math.degrees(alfa_rad)

        return alfa_st

