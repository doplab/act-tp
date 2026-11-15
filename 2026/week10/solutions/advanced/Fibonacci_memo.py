previous_fibonacci = {0:0, 1:1}

def fibonacci(number):
    global previous_fibonacci
    if number not in previous_fibonacci:
        previous_fibonacci[number] = fibonacci(number - 1) + fibonacci(number - 2)

    return previous_fibonacci[number]

if __name__ == "__main__":
    print(fibonacci(10))
