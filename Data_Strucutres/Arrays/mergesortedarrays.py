# [0,3,4,31] + [4,6,30] -> [0,3,4,4,6,30,31]
def merge_sorted_arrays(array1: list, array2: list):
    return sorted(array1.extend(array2))


print(merge_sorted_arrays([0, 3, 4, 31], [4, 6, 30]))
