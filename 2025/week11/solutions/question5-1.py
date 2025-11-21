def binary_search_recursive(key, array, low=0, high=None):
    if high is None:
        high = len(array) - 1

    # Base case: not found
    if low > high:
        return -1

    mid = (low + high) // 2

    if key < array[mid]:
        return binary_search_recursive(key, array, low, mid - 1)
    elif key > array[mid]:
        return binary_search_recursive(key, array, mid + 1, high)
    else:
        return mid

if __name__ == '__main__':
    L = [1,3,4,5,7,8,9,15]
    x = 5
    idx = binary_search_recursive(x, L)
    print(idx)

