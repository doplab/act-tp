def binary_search(A, k, p, q):
    if (q < p):
        return "NON" # array is empty so it doesn't contain k
    else:
        mid = (p+q)//2
    if (A[mid] == k):
        return "OUI"
    elif (A[mid] > k):
        return binary_search(A, k, p, mid-1)
    else: # A[mid] < k
        return binary_search(A, k, mid+1, q)
