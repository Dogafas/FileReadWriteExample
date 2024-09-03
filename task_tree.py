import os


def read_file_info(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()
    return file_path, len(lines), lines


def merge_files(file_names, output_file):
    file_info = [read_file_info(file_name) for file_name in file_names]
    file_info.sort(key=lambda x: x[1])  # Сортировка по количеству строк

    with open(output_file, 'w', encoding='utf-8') as out_file:
        for file_path, line_count, lines in file_info:
            out_file.write(f"{os.path.basename(file_path)}\n")
            out_file.write(f"{line_count}\n")
            out_file.writelines(lines)
            out_file.write("\n")  # Добавляем пустую строку между файлами


if __name__ == "__main__":
    file_names = ["1.txt", "2.txt", "3.txt"]
    output_file = "output.txt"
    merge_files(file_names, output_file)
