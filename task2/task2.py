import sys
import math


def read_circle_data(file_path):
    with open(file_path, "r") as f:
        x_center = float(f.readline().strip())
        y_center = float(f.readline().strip())
        radius = float(f.readline().strip())
    return x_center, y_center, radius


def read_points(file_path):
    points = []
    with open(file_path, "r") as f:
        for line in f:
            coordinates = line.split()
            points.append((float(coordinates[0]), float(coordinates[1])))
    return points


def point_position(x, y, x_center, y_center, radius):
    distance_squared = (x - x_center) ** 2 + (y - y_center) ** 2
    radius_squared = radius**2

    if math.isclose(distance_squared, radius_squared):
        return 0
    elif distance_squared < radius_squared:
        return 1
    else:
        return 2


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print(
            "Использование: python task2.py <путь к файлу с окружностью> <путь к файлу с точками>"
        )
        sys.exit(1)

    circle_file = sys.argv[1]
    points_file = sys.argv[2]

    x_center, y_center, radius = read_circle_data(circle_file)
    points = read_points(points_file)

    for x, y in points:
        result = point_position(x, y, x_center, y_center, radius)
        print(result)
