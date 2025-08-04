import cv2
import numpy as np
import matplotlib.pyplot as plt


def read_image(image_path):
    img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)  # Wczytujemy obraz jako skala szarości

    # Sprawdzamy czy obraz został poprawnie wczytany
    if img is None:
        raise ValueError("Unable to read the image. Please check the file path.")

    return img


def advancing_front(img, density=1.0):
    # Algorytm Canny do detekcji krawędzi
    edges = cv2.Canny(img, 100, 200)

    # Znajdujemy kontury
    contours, _ = cv2.findContours(edges, cv2.RETR_CCOMP, cv2.CHAIN_APPROX_SIMPLE)

    # Przekształcamy kontury do naszego formatu danych
    vertices = {}
    edges = []
    for contour in contours:
        idx = len(vertices) + 1
        for point in contour:
            x, y = point[0]
            vertices[idx] = (x, y)
            idx += 1
        for i in range(len(contour) - 1):
            edges.append((idx - len(contour) + i, idx - len(contour) + i + 1))
        edges.append((idx - 1, idx - len(contour)))  # Łączymy ostatni punkt z pierwszym, aby zamknąć kontur

    # Algorytm Advancing Front - przykładowa implementacja
    front_edges = []
    for edge in edges:
        v1, v2 = edge
        front_edges.append((v1, v2))

    # Modyfikacja frontu zgodnie z zagęszczeniem
    if density != 1.0:
        new_front_edges = []
        for edge in front_edges:
            v1, v2 = edge
            new_front_edges.append((v1, v2))
            new_front_edges.append((v2, v1))  # Dodanie dodatkowego odcinka

        front_edges = new_front_edges

    return front_edges, vertices


def create_mesh(front_edges, vertices, density=1.0):
    # Tworzymy siatkę na podstawie odcinków frontu
    mesh = []
    for edge in front_edges:
        v1, v2 = edge
        p1 = vertices[v1]
        p2 = vertices[v2]
        length = np.linalg.norm(np.array(p2) - np.array(p1))
        num_divisions = max(int(length * density), 1)
        x_values = np.linspace(p1[0], p2[0], num_divisions)
        y_values = np.linspace(p1[1], p2[1], num_divisions)
        for i in range(num_divisions - 1):
            mesh.append(((x_values[i], y_values[i]), (x_values[i + 1], y_values[i + 1])))

    return mesh


def visualize(img, vertices, edges=None, mesh=None):
    fig, ax = plt.subplots()

    # Wizualizacja obrazu
    ax.imshow(img, cmap='gray')

    # Wizualizacja konturu
    if edges:
        for edge in edges:
            v1, v2 = edge
            ax.plot([vertices[v1][0], vertices[v2][0]],
                    [vertices[v1][1], vertices[v2][1]], 'r-', linewidth=1.5)  # Grubsza linia

    # Wizualizacja siatki
    if mesh:
        for line in mesh:
            (x1, y1), (x2, y2) = line
            ax.plot([x1, x2], [y1, y2], 'g-', linewidth=0.5)  # Cieńsza linia

    ax.set_aspect('equal', 'box')
    ax.autoscale()
    plt.show()


def save_contour_image(img, vertices, edges, save_path):
    # Tworzymy obraz z konturami siatki
    contour_img = np.zeros_like(img)
    for edge in edges:
        v1, v2 = edge
        cv2.line(contour_img, vertices[v1], vertices[v2], (255, 255, 255), 1)  # Biały kolor konturu

    # Zapisujemy obraz z konturami
    cv2.imwrite(save_path, contour_img)


def main():
    # Wczytywanie obrazu JPG
    image_path = 'pacman_duch.jpg'
    try:
        img = read_image(image_path)
    except ValueError as e:
        print(e)
        return

    # Wyznaczanie odcinków frontu z różnymi parametrami
    front_edges_normal, vertices_normal = advancing_front(img, density=1.0)
    front_edges_dense, vertices_dense = advancing_front(img, density=2.0)

    # Tworzenie siatki na podstawie odcinków frontu
    mesh_normal = create_mesh(front_edges_normal, vertices_normal, density=0.1)
    mesh_dense = create_mesh(front_edges_dense, vertices_dense, density=0.1)

    # Wizualizacja
    print("Normal Density:")
    visualize(img, vertices_normal, front_edges_normal, mesh_normal)

    print("Dense Density:")
    visualize(img, vertices_dense, front_edges_dense, mesh_dense)

    # Zapisz obrazy z konturami siatki
    save_contour_image(img, vertices_normal, front_edges_normal, "contour_normal.png")
    save_contour_image(img, vertices_dense, front_edges_dense, "contour_dense.png")


if __name__ == "__main__":
    main()
