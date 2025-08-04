import numpy as np
import matplotlib.pyplot as plt
from scipy.spatial import Delaunay
import random
import time

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

def ccw(a, b, c):
    return (c.y - a.y) * (b.x - a.x) > (b.y - a.y) * (c.x - a.x)

def left_turn(p1, p2, p3):
    return ccw(p1, p2, p3)

def right_turn(p1, p2, p3):
    return not left_turn(p1, p2, p3)

def compare(p1, p2):
    if p1.y < p2.y:
        return -1
    elif p1.y > p2.y:
        return 1
    elif p1.x < p2.x:
        return -1
    elif p1.x > p2.x:
        return 1
    else:
        return 0

def triangle_quality(triangle):
    # Obliczanie jakości trójkąta na podstawie jego boków
    a = np.sqrt((triangle[0].x - triangle[1].x)**2 + (triangle[0].y - triangle[1].y)**2)
    b = np.sqrt((triangle[1].x - triangle[2].x)**2 + (triangle[1].y - triangle[2].y)**2)
    c = np.sqrt((triangle[2].x - triangle[0].x)**2 + (triangle[2].y - triangle[0].y)**2)
    s = (a + b + c) / 2
    area = np.sqrt(s * (s - a) * (s - b) * (s - c))
    quality = (3 * np.sqrt(3) * area) / (a**2 + b**2 + c**2)
    return quality

def triangulate(points):
    start_time = time.time()
    points.sort(key=lambda p: (p.x, p.y))
    stack = [points[0], points[1]]
    triangles = []
    for i in range(2, len(points)):
        while len(stack) >= 2 and right_turn(stack[-2], stack[-1], points[i]):
            triangles.append((stack[-2], stack[-1], points[i]))
            stack.pop()
        stack.append(points[i])
    end_time = time.time()
    execution_time = end_time - start_time
    return triangles, execution_time

def bowyer_watson(points):
    start_time = time.time()
    # Dodaj punkt fikcyjny w nieskończoność
    inf_point = np.array([np.mean(points[:, 0]), np.mean(points[:, 1])]) + 100*np.array([np.std(points[:, 0]), np.std(points[:, 1])])
    points = np.append(points, [inf_point], axis=0)
    triangles = Delaunay(points).simplices.tolist()

    # Usuń trójkąty zawierające punkt nieskończoności
    triangles = [tri for tri in triangles if len(set(tri) & {len(points) - 1}) == 0]

    # Usuń punkt nieskończoności
    points = np.delete(points, -1, axis=0)

    end_time = time.time()
    execution_time = end_time - start_time
    return triangles, execution_time

def plot_triangulation(points, triangles):
    # Plot points
    x = [point.x for point in points]
    y = [point.y for point in points]
    plt.plot(x, y, 'bo')

    # Plot triangles
    for triangle in triangles:
        triangle_x = [point.x for point in triangle + (triangle[0],)]
        triangle_y = [point.y for point in triangle + (triangle[0],)]
        plt.plot(triangle_x, triangle_y, 'r-')

    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title('Triangulation')
    plt.gca().set_aspect('equal', adjustable='box')
    plt.show()

def main():
    # Generowanie przykładowych punktów dla triangulacji
    num_points = 50
    min_val = 0
    max_val = 10
    points = np.random.rand(num_points, 2) * (max_val - min_val) + min_val

    # Triangulacja Delaunay'a za pomocą algorytmu Bowyera-Watsona
    triangles1, bw_execution_time = bowyer_watson(points)
    triangle_qualities1 = [triangle_quality([Point(*points[i]) for i in tri]) for tri in triangles1]

    # Triangulacja metodą "triangulate"
    points2 = [Point(x, y) for x, y in points]
    triangles2, tr_execution_time = triangulate(points2)
    triangle_qualities2 = [triangle_quality([point for point in tri]) for tri in triangles2]

    # Informacje o powstałych sympleksach
    num_triangles1 = len(triangles1)
    num_triangles2 = len(triangles2)
    min_quality1 = min(triangle_qualities1)
    max_quality1 = max(triangle_qualities1)
    median_quality1 = np.median(triangle_qualities1)
    min_quality2 = min(triangle_qualities2)
    max_quality2 = max(triangle_qualities2)
    median_quality2 = np.median(triangle_qualities2)

    # Informacje o czasie wykonania operacji triangulacji
    print("Triangulacja Delaunay'a (algorytm Bowyera-Watsona):")
    print("Liczba trójkątów:", num_triangles1)
    print("Najgorsza jakość trójkąta:", max_quality1)
    print("Najlepsza jakość trójkąta:", min_quality1)
    print("Mediana jakości trójkątów:", median_quality1)
    print("Czas wykonania:", bw_execution_time, "sekund")
    print()
    print("Triangulacja metodą 'triangulate':")
    print("Liczba trójkątów:", num_triangles2)
    print("Najgorsza jakość trójkąta:", max_quality2)
    print("Najlepsza jakość trójkąta:", min_quality2)
    print("Mediana jakości trójkątów:", median_quality2)
    print("Czas wykonania:", tr_execution_time, "sekund")

    # Plotowanie wyników
    fig, axes = plt.subplots(1, 2, figsize=(12, 6))

    # Triangulacja Delaunay'a za pomocą algorytmu Bowyera-Watsona
    axes[0].triplot(points[:, 0], points[:, 1], triangles1)
    axes[0].plot(points[:, 0], points[:, 1], 'o')
    axes[0].set_title('Triangulacja Delaunay\'a (algorytm Bowyera-Watsona)')
    axes[0].set_xlabel('X')
    axes[0].set_ylabel('Y')

    # Triangulacja metodą "triangulate"
    plot_triangulation(points2, triangles2)
    axes[1].set_title('Triangulacja "triangulate"')
    axes[1].set_xlabel('X')
    axes[1].set_ylabel('Y')

    plt.tight_layout()

if __name__ == "__main__":
    main()
