def recherche_binaire_recursive(key, array, low, high):
    # Base case: not found
    if low > high:
        return -1

    mid = (low + high) // 2

    if key < array[mid]:
        return recherche_binaire_recursive(key, array, low, mid - 1)
    elif key > array[mid]:
        return recherche_binaire_recursive(key, array, mid + 1, high)
    else:
        return mid

if __name__ == '__main__':
    liste = [1,3,4,5,7,8,9,15]
    key = 7
    idx = recherche_binaire_recursive(key, liste, 0, len(liste) - 1)
    print(idx)

