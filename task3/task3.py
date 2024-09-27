import sys
import json


def load_json(file_path):
    """Функция для загрузки данных из JSON файла."""
    with open(file_path, "r") as f:
        return json.load(f)


def save_json(data, file_path):
    """Функция для записи данных в JSON файл."""
    with open(file_path, "w") as f:
        json.dump(data, f, indent=4)


def fill_values(tests, results_dict):
    """Рекурсивная функция для заполнения поля 'value' в структуре тестов."""
    for test in tests:
        test_id = test["id"]
        if test_id in results_dict:
            test["value"] = results_dict[test_id]

        if "values" in test:
            fill_values(test["values"], results_dict)


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print(
            "Использование: python script.py <path_to_values_json> <path_to_tests_json> <path_to_report_json>"
        )
        sys.exit(1)

    values_file = sys.argv[1]
    tests_file = sys.argv[2]
    report_file = sys.argv[3]

    values_data = load_json(values_file)
    tests_data = load_json(tests_file)

    results_dict = {item["id"]: item["value"] for item in values_data["values"]}

    fill_values(tests_data["tests"], results_dict)

    save_json(tests_data, report_file)

    print(f"Отчет успешно сохранен в {report_file}")
