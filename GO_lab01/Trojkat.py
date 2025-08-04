import math
from Linia import Linia
class Trojkat:
    def __init__(self, wierzcholki):
        self.wierzcholki = wierzcholki

    def trojkat(self, linia):
        self.wierzcholki = []

        for i in range(3):
            for j in range(i + 1, 3):
                a1, b1, c1 = linia[i]
                a2, b2, c2 = linia[j]
                # Obliczenie współrzędnych punktu przecięcia dwóch prostych
                x = (b1 * c2 - b2 * c1) / (a1 * b2 - a2 * b1)
                y = (a2 * c1 - a1 * c2) / (a1 * b2 - a2 * b1)
                self.wierzcholki.append((x, y))

        return self.wierzcholki

    def pole_trojkata(self, a, b, c):
        ab = math.sqrt((b[0] - a[0]) ** 2 + (b[1] - a[1]) ** 2)
        bc = math.sqrt((c[0] - b[0]) ** 2 + (c[1] - b[1]) ** 2)
        ac = math.sqrt((c[0] - a[0]) ** 2 + (c[1] - a[1]) ** 2)

        p = (ab + bc + ac) / 2
        S = math.sqrt(p * (p - ab) * (p - bc) * (p - ac))

        return S


    def przynaleznosc_pkt_do_t_pole(self, p):
        a, b, c = self.wierzcholki[:3]
        S = self.pole_trojkata(a, b, c)
        S1 = self.pole_trojkata(a, b, p)
        S2 = self.pole_trojkata(a, c, p)
        S3 = self.pole_trojkata(b, c, p)
        print("S ", S)
        print("S1 ", S1)
        print("S2 ", S2)
        print("S3 ", S3)
        print("S1 + S2 + S3 ", S1 + S2 + S3)
        if (S < S1 + S2 + S3):
            print("Punkt znajduje się poza trójkątem")
            return False
        else:
            print("Punkt znajduje się wewnątrz trójkąta")
            return True

    def przynaleznosc_pkt_do_t_kat(self, p):
        linia = Linia(None, None, None, None)
        a, b, c = self.wierzcholki[:3]
        abp = linia.kat_m_liniami(p, a, b)
        acp = linia.kat_m_liniami(p, a, c)
        bcp = linia.kat_m_liniami(p, b, c)

        if abp + acp + bcp == 360:
            print("Punkt znajduje się wewnątrz trójkąta")
            return True
        else:
            print("Punkt znajduje się poza trójkątem")
            return False


