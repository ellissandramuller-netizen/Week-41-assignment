
def flatten_list(nested_list):
    flattened_list = []

    for n in nested_list:
        if isinstance(n, (list, tuple)):
            flattened_list.extend(flatten_list(n))
        else:
            flattened_list.append(n)

    return flattened_list

with open("log_4.txt", "r", encoding="latin-1") as file:
    content = file.read()

print(content)
