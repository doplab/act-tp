def recherche_binaire(key, array):
    low = 0
    high = len(array) - 1

    while low <= high:
        mid = (low + high) // 2

        if key < array[mid]:
            high = mid - 1
        elif key > array[mid]:
            low = mid + 1
        else:
            return mid

    return -1

if __name__ == '__main__':
    L = [1,3,4,5,7,8,9,15]
    x = 5
    idx = recherche_binaire(x, L)
    print(idx)
