def binary_search(my_list, search):
    min = 0
    max = len(my_list) - 1
    t = 0
    while min <= max:
        t += 1
        mid = (min + max) // 2
        item = my_list[mid]

        if search == item:
            print("t=", t)
            return mid
        elif search > item:
            min = mid + 1
        else:
            max = mid - 1

    return None




#          0, 1,  2,  3,  4,  5,  6,  7,  8,  9,  10, 11, 12, 13, 14, 15,  16,  17,  18,  19,  20,  21,  22,  23,  24,  25,  26,  27
my_list = [7, 15, 18, 21, 32, 34, 37, 39, 45, 48, 55, 60, 65, 70, 86, 101, 112, 119, 120, 151, 152, 161, 170, 172, 200, 206, 223, 232]

print(binary_search(my_list, 119))
