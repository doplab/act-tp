def fibonacci_i(n):
    if n == 0 or n == 1:
        return n
    else:
        old_fib = 1
        new_fib = 1
        for i in range(n - 2):
            temp = new_fib
            new_fib = new_fib + old_fib
            old_fib = temp
        return new_fib


if __name__ == "__main__":
    print(fibonacci_i(9))
