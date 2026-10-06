
def flatten_list(nested_list):
    flattened_list = []

    for n in nested_list:
        if isinstance(n, (list, tuple)):
            flatten_list(n)
        else:
            flattened_list.append(n)

    return flattened_list    