import sys


def circular_path(n, m):

    circular_array = list(range(1, n + 1))

    path = []
    current_position = 0
    visited_positions = set()

    while current_position not in visited_positions:

        path.append(circular_array[current_position])
        visited_positions.add(current_position)

        current_position = (current_position + m - 1) % n

    return path


if __name__ == "__main__":

    if len(sys.argv) != 3:
        print("Использование: python script.py <n> <m>")
        sys.exit(1)

    n = int(sys.argv[1])
    m = int(sys.argv[2])

    result = circular_path(n, m)
    print("".join(map(str, result)))
