import math
import matplotlib.pyplot as plt

class Wielokat:
    def __init__(self, wierzcholki):
        self.wierzcholki = wierzcholki
        self.liczba_wierzcholkow = len(wierzcholki)

    def wyswietl_wierzcholki(self):
        print("Współrzędne wierzchołków wielokąta:")
        for i, wierzcholek in enumerate(self.wierzcholki):
            print(f"Wierzchołek {i + 1}: ({wierzcholek[0]}, {wierzcholek[1]})")

    def obwod(self):
        obwod = 0
        for i in range(self.liczba_wierzcholkow):
            x1, y1 = self.wierzcholki[i]
            if i == self.liczba_wierzcholkow - 1:
                x2, y2 = self.wierzcholki[0]
            else:
                x2, y2 = self.wierzcholki[i + 1]
            obwod += ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
        return obwod

    def przynaleznosc_pkt_do_w(self, punkt):
        x, y = punkt
        przeciecia = 0
        n = len(self.wierzcholki)
        for i in range(n):
            x1, y1 = self.wierzcholki[i]
            x2, y2 = self.wierzcholki[(i + 1) % n]
            if y1 == y2:  # Ignoruj poziome krawędzie
                continue
            if min(y1, y2) < y <= max(y1, y2):
                x_przeciecia = (y - y1) * (x2 - x1) / (y2 - y1) + x1
                if x_przeciecia > x:
                    przeciecia += 1
        if przeciecia % 2 == 1:
            print("Punkt należy do wielokąta")
        else:
            print("Punkt nie należy do wielokąta")

        return przeciecia
