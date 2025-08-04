from Trojkat import Trojkat
class OtoczkaWypukla:
    def __init__(self, points):
        self.points = points

    def orientation(self, p, q, r):
        val = (q.y - p.y) * (r.x - q.x) - (q.x - p.x) * (r.y - q.y)
        if val == 0:
            return 0  # współliniowe
        elif val > 0:
            return 1  # zgodnie z ruchem wskazówek zegara
        else:
            return 2  # przeciwnie do ruchu wskazówek zegara

    def jarvis_convex_hull(self):
        points = self.points
        n = len(points)
        if n < 3:
            return []

        hull = []
        l = 0
        for i in range(1, n):
            if points[i].x < points[l].x:
                l = i

        p = l
        while True:
            hull.append(points[p])

            q = (p + 1) % n
            for i in range(n):
                if self.orientation(points[p], points[i], points[q]) == 2:
                    q = i

            p = q

            if p == l:
                break

        return hull


    def graham_scan(self, points):
        n = len(points)
        if n < 3:
            return []

        # Sortowanie punktów według współrzędnej y, a dla punktów o tej samej współrzędnej y - według współrzędnej x.
        sorted_points = sorted(points, key=lambda point: (point.y, point.x))

        # Tworzenie górnej części otoczki wypukłej
        upper_hull = []
        for p in sorted_points:
            while len(upper_hull) >= 2 and self.orientation(upper_hull[-2], upper_hull[-1], p) != 2:
                upper_hull.pop()
            upper_hull.append(p)

        # Tworzenie dolnej części otoczki wypukłej
        lower_hull = []
        for p in reversed(sorted_points):
            while len(lower_hull) >= 2 and self.orientation(lower_hull[-2], lower_hull[-1], p) != 2:
                lower_hull.pop()
            lower_hull.append(p)

        # Łączenie górnej i dolnej części otoczki wypukłej
        convex_hull = upper_hull[:-1] + lower_hull[:-1]

        return convex_hull