def fibonacci_search(lst, target):
    size = len(lst)

    start = -1

    f0 = 0
    f1 = 1
    f2 = 1
    while (f2 < size):
        f0 = f1
        f1 = f2
        f2 = f1 + f0

    t = 0

    while (f2 > 1):
        t += 1
        index = min(start + f0, size - 1)
        if lst[index] < target:
            f2 = f1
            f1 = f0
            f0 = f2 - f1
            start = index
        elif lst[index] > target:
            f2 = f0
            f1 = f1 - f0
            f0 = f2 - f1
        else:
            print("t=", t)
            return index
    if (f1) and (lst[size - 1] == target):
        return size - 1
    return None
lst = [7, 15, 18, 21, 32, 34, 37, 39, 45, 48, 55, 60, 65, 70, 86, 101, 112, 119, 120, 151, 152, 161, 170, 172, 200, 206, 223, 232]

print(fibonacci_search(lst, 101))