from Punkt import Punkt
from Linia import Linia
from Trojkat import Trojkat
from  Wielokat import Wielokat
from OtoczkaWypukla import OtoczkaWypukla
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon
import numpy as np
import random
def menu():
    """
    print("1. Wyznaczenie równanie prostej, do której należy dana linia")
    print("2. Sprawdzenie przynaleźności punktu do prostej")
    print("3. Sprawdzenie przynaleźności punktu do odcinka")
    print("4. Określenie położenia punktu względem prostej")
    print("5. Dokonanie translacji linii o podany wektor")
    print("6. Dokonanie odbicia danego punktu względem linii")
    print("7. Punkt przecięcia 2 prostych")
    print("8. Punkt przecięcia 2 prostych b")
    print("9. Oblicz odległość punktu od prostej")
    print("10. Narysuj trójkąt ograniczony tymi trzema prostymi")
    print("11. Pole trojkąta")
    print("12. Kąt między dwoma liniami")
    print("13. Sprawdzanie przynależności punktu do trójkąta - pole")
    print("14. Sprawdzanie przynależności punktu do trójkąta - kąt")
    print("15. Czy punkt należy do wielokąta")
    """
    print("16. Otoczka wypukla - Jarvis")
    print("17. Otoczka wypukla - Graham")
    print("0. Wyjście")


def wyznaczenie_r_pr():
    punkt1x = float(input("Podaj współrzędną x pierwszego punktu: "))
    punkt1y = float(input("Podaj współrzędną y pierwszego punktu: "))
    punkt2x = float(input("Podaj współrzędną x drugiego punktu: "))
    punkt2y = float(input("Podaj współrzędną y drugiego punktu: "))


    linia = Linia(punkt1x, punkt1y, punkt2x, punkt2y)
    print(linia.punkt1x)
    print(linia.punkt1y)
    print(linia.punkt2x)
    print(linia.punkt2y)
    a, b = linia.wyznacz_rownanie_prostej()
    print(a, b)

    # rysowanie?????
    if a is None:
        x_values = [punkt1x, punkt1x]
        y_values = [min(punkt1y, punkt2y), max(punkt1y, punkt2y)]
    else:
        x_values = [min(punkt1x, punkt2x), max(punkt1x, punkt2x)]
        y_values = [a * x + b for x in x_values]

    plt.plot(x_values, y_values, label=f'y = {a}x + {b}')

    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Wyznaczenie równania prostej')
    plt.axhline(0, color='black', linewidth=0.5)
    plt.axvline(0, color='black', linewidth=0.5)
    plt.grid(color='gray', linestyle='--', linewidth=0.5)
    plt.legend()
    plt.show()

def spr_przynaleznosci_pkt_do_prostej():
    a = float(input("Podaj a rownania prostej kierunkowej: "))
    b = float(input("Podaj b rownania prostej kierunkowej: "))
    x = float(input("Podaj wspolrzedna x punktu: "))
    y = float(input("Podaj wspolrzedna y punktu: "))

    punkt = Punkt(x, y)
    print(punkt.x)
    print(punkt.y)
    punkt.przynaleznosc_pkt_do_prostej(a, b)

    # rysowanie
    przynaleznosc = punkt.przynaleznosc_pkt_do_prostej(a, b)
    print("Czy punkt należy do prostej? ", przynaleznosc)
    x_values = range(-10, 11)
    y_values = np.array([a*x + b for x in x_values])
    plt.plot(x_values, y_values, label=f'y = {a}x + {b}')
    plt.scatter(punkt.x, punkt.y, color='red', label='Punkt')

    # Dodanie punktu, jeśli należy do prostej
    if przynaleznosc:
        plt.text(punkt.x, punkt.y, 'Punkt na prostej', fontsize=12, ha='right')

    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Sprawdzenie przynależności punktu do prostej')
    plt.axhline(0, color='black', linewidth=0.5)
    plt.axvline(0, color='black', linewidth=0.5)
    plt.grid(color='gray', linestyle='--', linewidth=0.5)
    plt.legend()
    plt.show()

def spr_przynaleznosci_pkt_do_odcinka():
    x_punkt1 = float(input("Podaj współrzędną x pierwszego punktu: "))
    y_punkt1 = float(input("Podaj współrzędną y pierwszego punktu: "))
    x_punkt2 = float(input("Podaj współrzędną x drugiego punktu: "))
    y_punkt2 = float(input("Podaj współrzędną y drugiego punktu: "))
    x = float(input("Podaj współrzędną x punktu: "))
    y = float(input("Podaj współrzędną y punktu: "))

    punkt = Punkt(x, y)
    print(punkt.przynaleznosc_do_odcinka(x_punkt1, y_punkt1, x_punkt2, y_punkt2))

    # rysowanie
    xpoints = np.array([x_punkt1, x_punkt2])
    ypoints = np.array([y_punkt1, y_punkt2])
    plt.plot(xpoints, ypoints)
    plt.plot(x, y, marker = 'o', ms = 5)
    plt.show()


def okreslenie_polozenia_punktu_wzg_prostej():
    x_punkt1 = float(input("Podaj współrzędną x pierwszego punktu: "))
    y_punkt1 = float(input("Podaj współrzędną y pierwszego punktu: "))
    x_punkt2 = float(input("Podaj współrzędną x drugiego punktu: "))
    y_punkt2 = float(input("Podaj współrzędną y drugiego punktu: "))
    x = float(input("Podaj wspolrzedna x punktu: "))
    y = float(input("Podaj wspolrzedna y punktu: "))

    punkt = Punkt(x, y)
    print(punkt.polozenie_pkt_wzgl_prostej(x_punkt1, y_punkt1, x_punkt2, y_punkt2))

    # rysowanie
    xpoints = np.array([x_punkt1, x_punkt2])
    ypoints = np.array([y_punkt1, y_punkt2])
    plt.plot(xpoints, ypoints)
    plt.plot(x, y, marker = 'o', ms = 5)
    plt.show()


def transjacja():
    x_punkt1 = float(input("Podaj współrzędną x pierwszego punktu linii: "))
    y_punkt1 = float(input("Podaj współrzędną y pierwszego punktu linii: "))
    x_punkt2 = float(input("Podaj współrzędną x drugiego punktu linii: "))
    y_punkt2 = float(input("Podaj współrzędną y drugiego punktu linii: "))
    v = int(input("Podaj pierwszą wartość wektora: "))
    u = int(input("Podaj pierwszą wartość wektora: "))

    wektor = [v, u]

    linia = Linia(x_punkt1, y_punkt1, x_punkt2, y_punkt2)
    x1p, y1p, x2p, y2p = linia.translacja(wektor)


    # rysowanie
    xpoints = np.array([x_punkt1, x_punkt2])
    ypoints = np.array([y_punkt1, y_punkt2])
    xp = np.array([x1p, x2p])
    yp = np.array([y1p, y2p])

    plt.plot(xpoints, ypoints)
    plt.plot(xp, yp)
    plt.show()

def odbicie_punktu_wzgl_linii():
    x_punkt1 = float(input("Podaj współrzędną x pierwszego punktu: "))
    y_punkt1 = float(input("Podaj współrzędną y pierwszego punktu: "))
    x_punkt2 = float(input("Podaj współrzędną x drugiego punktu: "))
    y_punkt2 = float(input("Podaj współrzędną y drugiego punktu: "))
    x = float(input("Podaj wspolrzedna x punktu: "))
    y = float(input("Podaj wspolrzedna y punktu: "))

    punkt = Punkt(x, y)
    x2, y2 = punkt.odbicie_wzgl_linii(x_punkt1, y_punkt1, x_punkt2, y_punkt2)
    print(punkt.odbicie_wzgl_linii(x_punkt1, y_punkt1, x_punkt2, y_punkt2))

    # rysowanie
    plt.plot([x_punkt1, x_punkt2], [y_punkt1, y_punkt2], label='Linia')
    plt.plot(x, y, marker='o', ms=5, label='Punkt')
    plt.plot(x2, y2, marker='o', ms=5, label='Odbity punkt')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title('Odbicie punktu względem linii')
    plt.legend()
    plt.grid(True)
    plt.axis('equal')
    plt.show()


def punkt_przeciecia_prostych_a():
    a1 = float(input("Podaj A równanie ogólnego pierwszej prostej: "))
    b1 = float(input("Podaj B równanie ogólnego pierwszej prostej: "))
    c1 = float(input("Podaj C równanie ogólnego pierwszej prostej: "))
    a2 = float(input("Podaj A równanie ogólnego drugiej prostej: "))
    b2 = float(input("Podaj B równanie ogólnego drugiej prostej: "))
    c2 = float(input("Podaj C równanie ogólnego drugiej prostej: "))

    linia = Linia(None, None, None, None)
    x, y = linia.punkt_przecięcia_dwoch_prostych(a1, b1, c1, a2, b2, c2)
    print(linia.punkt_przecięcia_dwoch_prostych(a1, b1, c1, a2, b2, c2))

    # rysowanie
    x_range = np.linspace(-10, 10, 400)

    # Obliczenie współrzędnych y dla każdej prostej
    y1 = (-a1 * x_range - c1) / b1
    y2 = (-a2 * x_range - c2) / b2

    # Rysowanie prostych
    plt.plot(x_range, y1, label=f"{a1}x + {b1}y + {c1} = 0")
    plt.plot(x_range, y2, label=f"{a2}x + {b2}y + {c2} = 0")
    plt.plot(x, y, 'ro', label="Punkt przecięcia")

    # Ustawienie etykiet i tytułu
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Rysowanie prostych')

    # Dodanie legendy
    plt.legend()

    # Pokazanie wykresu
    plt.grid(True)
    plt.axhline(0, color='black', linewidth=0.5)
    plt.axvline(0, color='black', linewidth=0.5)
    plt.show()


def punkt_przeciecia_prostych_b():
    p1_start_x = float(input("Podaj współrzędną x początkowego punkty pierwszej linii: "))
    p1_start_y = float(input("Podaj współrzędną y początkowego punkty pierwszej linii: "))
    p1_end_x = float(input("Podaj współrzędną x końcowego punkty pierwszej linii: "))
    p1_end_y = float(input("Podaj współrzędną y końcowego punkty pierwszej linii: "))
    p2_start_x = float(input("Podaj współrzędną x początkowego punkty drugiej linii: "))
    p2_start_y = float(input("Podaj współrzędną y początkowego punkty drugiej linii: "))
    p2_end_x = float(input("Podaj współrzędną x końcowego punkty drugiej linii: "))
    p2_end_y = float(input("Podaj współrzędną y końcowego punkty drugiej linii: "))

    p1_start = [p1_start_x, p1_start_y]
    p1_end = [p1_end_x, p1_end_y]
    p2_start = [p2_start_x, p2_start_y]
    p2_end = [p2_end_x, p2_end_y]

    linia = Linia(None, None, None, None)
    x, y = linia.punkt_przeciecia_dwoch_prostych_b(p1_start, p1_end, p2_start, p2_end)
    print(linia.punkt_przeciecia_dwoch_prostych_b(p1_start, p1_end, p2_start, p2_end))

    # rysowanie
    x1V = (p1_start[0], p1_end[0])
    y1V = (p1_start[1], p1_end[1])
    x2V = (p2_start[0], p2_end[0])
    y2V = (p2_start[1], p2_end[1])
    plt.plot(x1V, y1V, 'b-', label='Linia 1')

    # Rysowanie linii 2
    plt.plot(x2V, y2V, 'g-', label='Linia 2')

    # Obliczenie punktu przecięcia
    x, y = linia.punkt_przeciecia_dwoch_prostych_b(p1_start, p1_end, p2_start, p2_end)
    plt.plot(x, y, marker = 'o', label='Punkt przecięcia')

    # Ustawienia wykresu
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Proste z punktem przecięcia')
    plt.legend()
    plt.grid(True)
    plt.axhline(0, color='black', linewidth=0.5)
    plt.axvline(0, color='black', linewidth=0.5)
    plt.show()


def odleglosc_punktu_od_prostej():
    a = float(input("Podaj A równanie ogólnego prostej: "))
    b = float(input("Podaj B równanie ogólnego prostej: "))
    c = float(input("Podaj C równanie ogólnego prostej: "))
    x = float(input("Podaj wspolrzedna x punktu: "))
    y = float(input("Podaj wspolrzedna y punktu: "))

    punkt = Punkt(x, y)
    odleglosc = punkt.odl_punkt_prosta(a, b, c)

    # rysowanie
    xp = np.linspace(-10, 10, 400)
    yp = (-c - a * xp) / b

    # Rysowanie wykresu
    plt.figure(figsize=(8, 6))

    # Prosta
    plt.plot(xp, yp, 'b-', label='Prosta: {}x + {}y + {} = 0'.format(a, b, c))

    # Punkt
    plt.scatter(x, y, color='red', label='Punkt: ({}, {})'.format(x, y))

    # Linia łącząca punkt z prosta
    plt.plot([x, x - a * odleglosc], [y, y - b * odleglosc], linestyle='--', color='green', label='Odległość = {:.2f}'.format(odleglosc))


    # Ustawienie etykiet osi i tytułu
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Odległość punktu od prostej')
    plt.grid(True)
    plt.axis('equal')
    plt.legend()

    # Wyświetlenie wykresu
    plt.show()


def trojkat():
    a1 = float(input("Podaj A równanie ogólnego pierwszej prostej: "))
    b1 = float(input("Podaj B równanie ogólnego pierwszej prostej: "))
    c1 = float(input("Podaj C równanie ogólnego pierwszej prostej: "))
    a2 = float(input("Podaj A równanie ogólnego drugiej prostej: "))
    b2 = float(input("Podaj B równanie ogólnego drugiej prostej: "))
    c2 = float(input("Podaj C równanie ogólnego drugiej prostej: "))
    a3 = float(input("Podaj A równanie ogólnego trzeciej prostej: "))
    b3 = float(input("Podaj B równanie ogólnego trzeciej prostej: "))
    c3 = float(input("Podaj C równanie ogólnego trzeciej prostej: "))

    linia_wsp = [(a1, b1, c1), (a2, b2, c2), (a3, b3, c3)]
    trojkat = Trojkat(linia_wsp)
    trojkat.trojkat(linia_wsp)

    # rysowanie
    plt.figure(figsize=(8, 6))
    plt.plot([trojkat.wierzcholki[0][0], trojkat.wierzcholki[1][0]], [trojkat.wierzcholki[0][1], trojkat.wierzcholki[1][1]], 'b-')
    plt.plot([trojkat.wierzcholki[1][0], trojkat.wierzcholki[2][0]], [trojkat.wierzcholki[1][1], trojkat.wierzcholki[2][1]], 'b-')
    plt.plot([trojkat.wierzcholki[2][0], trojkat.wierzcholki[0][0]], [trojkat.wierzcholki[2][1], trojkat.wierzcholki[0][1]], 'b-')
    plt.scatter([vertex[0] for vertex in trojkat.wierzcholki], [vertex[1] for vertex in trojkat.wierzcholki], color='red', zorder=5)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Trójkąt')
    plt.grid(True)
    plt.axis('equal')
    plt.show()

def pole_trojkata():
    a_x = float(input("Podaj współrzędną x dla punktu A: "))
    a_y = float(input("Podaj współrzędną y dla punktu A: "))
    b_x = float(input("Podaj współrzędną x dla punktu B: "))
    b_y = float(input("Podaj współrzędną y dla punktu B: "))
    c_x = float(input("Podaj współrzędną x dla punktu C: "))
    c_y = float(input("Podaj współrzędną y dla punktu C: "))

    trojkat_obj = Trojkat([])
    pole = trojkat_obj.pole_trojkata((a_x, a_y), (b_x, b_y), (c_x, c_y))
    print("Pole trójkąta: ", pole)

    # Rysowanie trójkąta
    x = [a_x, b_x, c_x, a_x]
    y = [a_y, b_y, c_y, a_y]

    plt.figure()
    plt.plot(x, y, 'b-')
    plt.fill(x, y, color='lightblue')
    plt.scatter(x, y, color='red')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Trójkąt ABC')
    plt.grid(True)
    plt.axis('equal')
    plt.show()

def kat_m_liniami():
    p1_start = (1, 1)
    p1_end = (4, 5)
    p2_start = (2, 3)
    p2_end = (6, 2)

    # Stworzenie obiektów linii
    line1 = Linia(p1_start[0], p1_start[1], p1_end[0], p1_end[1])
    line2 = Linia(p2_start[0], p2_start[1], p2_end[0], p2_end[1])

    # Rysowanie linii
    plt.plot([p1_start[0], p1_end[0]], [p1_start[1], p1_end[1]], label='Linia 1')
    plt.plot([p2_start[0], p2_end[0]], [p2_start[1], p2_end[1]], label='Linia 2')

    # Obliczenie punktu przecięcia
    przeciecie = line1.punkt_przeciecia_dwoch_prostych_b(p1_start, p1_end, p2_start, p2_end)

    if przeciecie is None:
        print("Linie są równoległe, brak kąta między nimi.")
        return

    # Rysowanie punktu przecięcia
    plt.scatter(przeciecie[0], przeciecie[1], color='red', label='Przecięcie')

    # Obliczenie kąta między liniami
    angle = line2.kat_m_liniami(przeciecie, p1_start, p2_start)

    if angle is not None:
        # Dodanie adnotacji z kątem
        plt.annotate(text=f'Kąt: {angle:.2f}°', xy=(przeciecie[0], przeciecie[1]),
                     xytext=(przeciecie[0] + 1, przeciecie[1] + 1), arrowprops=dict(facecolor='black', arrowstyle='->'))

    plt.xlabel('X')
    plt.ylabel('Y')
    plt.legend()
    plt.grid()
    plt.show()

def przynaleznosc_pkt_do_t_pole():
    a = (12, 54)
    b = (3, 8)
    c = (32, 4)
    p = (12, 10)

    wierzcholki = (a, b, c, p)
    trojkat = Trojkat(wierzcholki)
    przynaleznosc = trojkat.przynaleznosc_pkt_do_t_pole(p)
    print(przynaleznosc)


    plt.figure()
    # trójkąt
    plt.fill([a[0], b[0], c[0], a[0]], [a[1], b[1], c[1], a[1]], color='lightblue', label='Trójkąt')

    #  punkt
    plt.scatter(p[0], p[1], color='red', label='Punkt p')

    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title('Przynależność punktu do trójkąta')
    plt.legend()
    plt.grid()
    plt.show()

def przynaleznosc_pkt_do_t_kat():
    a = (12, 54)
    b = (3, 8)
    c = (32, 4)
    p = (12, 3)

    wierzcholki = (a, b, c, p)
    trojkat = Trojkat(wierzcholki)
    przynaleznosc = trojkat.przynaleznosc_pkt_do_t_kat(p)
    print(przynaleznosc)


    plt.figure()
    # trójkąt
    plt.fill([a[0], b[0], c[0], a[0]], [a[1], b[1], c[1], a[1]], color='lightblue', label='Trójkąt')

    #  punkt
    plt.scatter(p[0], p[1], color='red', label='Punkt p')

    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title('Przynależność punktu do trójkąta')
    plt.legend()
    plt.grid()
    plt.show()

def pkt_w_wielokacie():
    wierzcholki = [(0, 2), (1, 1), (3, 2), (3.5, 6), (6, 7), (6.5, 2), (5, 5), (4, 1), (8, 1.5), (9, 5), (10, 0), (11, 7), (4, 10)]  # Wierzchołki kwadratu
    punkt = (10, 0)

    wielokat = Wielokat(wierzcholki)
    nalezy = wielokat.przynaleznosc_pkt_do_w(punkt)
    print(nalezy)

    fig, ax = plt.subplots()
    wielokat = Polygon(wierzcholki, closed=True, fill=None, edgecolor='r')
    ax.add_patch(wielokat)
    ax.plot(punkt[0], punkt[1], 'bo')

    # Ustawienie zakresu osi
    min_x = min(wierzcholki, key=lambda x: x[0])[0]
    max_x = max(wierzcholki, key=lambda x: x[0])[0]
    min_y = min(wierzcholki, key=lambda x: x[1])[1]
    max_y = max(wierzcholki, key=lambda x: x[1])[1]
    ax.set_xlim(min_x - 1, max_x + 1)
    ax.set_ylim(min_y - 1, max_y + 1)

    ax.set_aspect('equal', adjustable='box')

    plt.grid()
    plt.show()

def read_points_from_file(filename):
    points = []
    with open(filename, 'r') as file:
        # Wczytaj liczbę punktów z pierwszej linii
        num_points = int(file.readline())

        # Wczytaj współrzędne punktów z kolejnych linii
        for _ in range(num_points):
            line = file.readline().strip()
            if line:
                parts = line.split()
                if len(parts) >= 2:
                    try:
                        x = float(parts[0])
                        y = float(parts[1])
                        points.append(Punkt(x, y))
                    except ValueError:
                        print(f"Ignorowanie niepoprawnej linii: {line}")
                else:
                    print(f"Ignorowanie niepoprawnej linii: {line}")
    return points

def plot_convex_hull(points, convex_hull):
    plt.figure()
    ax = plt.gca()
    ax.set_aspect('equal', adjustable='box')

    # rysowanie punktów
    xs = [point.x for point in points]
    ys = [point.y for point in points]
    plt.plot(xs, ys, 'bo')

    # rysowanie otoczki wypukłej
    hull_xs = [point.x for point in convex_hull + [convex_hull[0]]]
    hull_ys = [point.y for point in convex_hull + [convex_hull[0]]]
    plt.plot(hull_xs, hull_ys, 'r-')

    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title('Otoczka wypukła')
    plt.grid(True)
    plt.show()

def Jarvis():
    filename = "ksztalt_2.txt"
    points = read_points_from_file(filename)
    otoczka = OtoczkaWypukla(points)
    convex_hull = otoczka.jarvis_convex_hull()
    plot_convex_hull(points, convex_hull)

def Graham():
    filename = "ksztalt_3.txt"
    points = read_points_from_file(filename)
    otoczka = OtoczkaWypukla(points)
    hull_points = otoczka.graham_scan(points)
    plot_convex_hull(points, hull_points)


def generate_coordinates(filename):
    # Otwórz plik do zapisu
    with open(filename, "w") as file:
        # Nagłówek
        file.write("1000\n")

        # Generuj i zapisuj 1000 losowych par współrzędnych
        for _ in range(1000):
            x = random.randint(0, 100)
            y = random.randint(0, 100)
            file.write(f"{x} {y}\n")




def main():
    menu()
    wybor = int(input("Twój wybór: "))

    while wybor != 0:
        if wybor == 0:
            exit()
        elif wybor == 1:
            wyznaczenie_r_pr()
        elif wybor == 2:
            spr_przynaleznosci_pkt_do_prostej()
        elif wybor == 3:
            spr_przynaleznosci_pkt_do_odcinka()
        elif wybor == 4:
            okreslenie_polozenia_punktu_wzg_prostej()
        elif wybor == 5:
            transjacja()
        elif wybor == 6:
            odbicie_punktu_wzgl_linii()
        elif wybor == 7:
            punkt_przeciecia_prostych_a()
        elif wybor == 8:
            punkt_przeciecia_prostych_b()
        elif wybor == 9:
            odleglosc_punktu_od_prostej()
        elif wybor == 10:
            trojkat()
        elif wybor == 11:
            pole_trojkata()
        elif wybor == 12:
            kat_m_liniami()
        elif wybor == 13:
            przynaleznosc_pkt_do_t_pole()
        elif wybor == 14:
            przynaleznosc_pkt_do_t_kat()
        elif wybor == 15:
            pkt_w_wielokacie()
        elif wybor == 16:
            Jarvis()
        elif wybor == 17:
            Graham()
        elif wybor == 18:
            generate_coordinates("coordinates.txt")
        else:
            print("Wybór spoza listy")

        print()
        menu()
        wybor = int(input("Twój wybór: "))



def main2():
    xpoints = np.array([0, 20])
    ypoints = np.array([0, 20])
    plt.plot(xpoints, ypoints)
    plt.show()



if __name__ == "__main__":
    main()
