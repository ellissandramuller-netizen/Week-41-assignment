
def flatten_list(nested_list):
    flattened_list = []

    for n in nested_list:
        if isinstance(n, (list, tuple)):
            flattened_list.extend(flatten_list(n))
        else:
            flattened_list.append(n)

    return flattened_list


file_encodings = {
    "log_1.txt": "utf-8",
    "log_2.txt": "utf-8-sig",
    "log_3.txt": "utf-16",
    "log_4.txt": "latin-1"
}

def sort_error_logs(encodings):

    log_lines = []

    for filename, encoding in file_encodings.items():
        with open(filename, 'r', encoding=encoding) as file:
            content = file.readlines()
            for line in content:
                if line.startswith("["):
                    log_lines.append(line)

    with open('combined_lines.txt', 'w', encoding='utf-8-sig') as file:
        for line in log_lines:
            file.write(line)

sort_error_logs(file_encodings)
