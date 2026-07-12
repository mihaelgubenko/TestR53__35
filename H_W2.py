# 1.
def print_list_reverse(lst):
    if lst is None or not isinstance(lst, list) or len(lst) == 0:
        print("Wrong list")
    else:
        print(lst[::-1])

print_list_reverse({1, 2, 3, 4})

# 2.
def is_valid (point):
    if point is None or point ==():
        return None
    if point is not isinstance(point, tuple) or len(point) != 2:
        return False
    return isinstance(point[0], (int, float)) and isinstance(point[1], (int, float))
is_valid((3,5))

# 3.

def print_sub_revers(lst, start, finish):
    if lst is None or not isinstance(lst, list) or len(lst) == 0:
        print("Wrong args")
        return

    if not isinstance(start, int) or not isinstance(finish, int):
        print("Wrong args")
        return

    if start < 0 or finish < 0 or start >= len(lst) or finish >= len(lst) or start > finish:
        print("Wrong args")
        return

    result = lst[:start] + lst[start:finish + 1][::-1] + lst[finish + 1:]
    print(result)

print_sub_revers([1, 2, 3, 4, 5, 6], 1, 3)


