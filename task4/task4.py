import sys


def read_numbers_from_file(file_path):
    """Чтение массива чисел из файла."""
    with open(file_path, "r") as f:
        numbers = []
        for line in f:
            numbers.extend(map(int, line.split()))
    return numbers


def min_moves_to_equal(nums):
    """Вычисление минимального количества ходов для приведения всех чисел к медиане."""
    nums.sort()
    median = nums[len(nums) // 2]
    moves = sum(abs(num - median) for num in nums)
    return moves


if __name__ == "__main__":

    if len(sys.argv) != 2:
        print("Использование: python task4.py <путь_к_файлу>")
        sys.exit(1)

    file_path = sys.argv[1]
    nums = read_numbers_from_file(file_path)

    if not nums:
        print("Файл пуст или содержит некорректные данные")
        sys.exit(1)

    result = min_moves_to_equal(nums)
    print(result)
