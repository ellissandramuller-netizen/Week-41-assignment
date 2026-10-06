
def flatten_list(nested_list):
    flattened_list = []

    for n in nested_list:
        if isinstance(n, (list, tuple)):
            flattened_list.extend(flatten_list(n))
        else:
            flattened_list.append(n)

    return flattened_list    

test_list = [18, [10, [5]], (802, 80), "passord"]
print(flatten_list(test_list))