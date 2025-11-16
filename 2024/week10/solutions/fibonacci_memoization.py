counter = 0
previous_fibonacci = {0:0, 1:1}

def fibonacci(number, previous):
    global counter
    counter += 1
    if number not in previous:
        previous[number] = fibonacci(number - 1, previous) + fibonacci(number - 2, previous)
        print(previous)

    return previous[number]

if __name__ == "__main__":
    print(fibonacci(50, previous=previous_fibonacci))