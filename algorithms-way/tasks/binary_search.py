import numpy as np


def find_index(lst, num):
    """
    Попробуйте написать функцию, возвращающую индекс искомого элемента в отсортированном по возрастанию массиве
    (если таких несколько, то индекс первого из них).
    """
    first = 0
    last = len(lst) - 1

    while first <= last:
        mid = (first + last) // 2
        if lst[mid] == num:
            return mid
        elif lst[mid] > num:
            last = mid-1
        else:
            first = mid+1
    return -1


if __name__ == '__main__':
    for i in range(1, 10):
        arr = np.sort(np.random.randint(0, i, i))
        find = np.random.randint(0, i)
        idx_ = find_index(arr, find)
        idx_bool = False if idx_ == -1 else True

        if idx_bool != (find in arr):
            print(f'-------bad index------')
            print(f'arr is: {arr}')
            print(f'find val is: {find}')
            print(f'idx is: {idx_}')
        elif idx_ != -1 and find != arr[idx_]:
            print(f'-------bad value------')
            print(f'arr is: {arr}')
            print(f'find val is: {find}')
            print(f'idx is: {idx_}')
