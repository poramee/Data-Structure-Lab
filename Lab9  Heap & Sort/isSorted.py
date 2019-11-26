def isSorted(list):
    for i in range(0, len(list) - 1):
        if list[i + 1] < list[i]:
            return False
    return True
