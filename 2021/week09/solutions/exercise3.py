def displayOddNumbers(limit):
    for nb in range(limit+1):
        if nb % 2 == 1:
            print(nb)

limit = int(input("What is the limit of the function displayOddNumbers(limit)? "))

print("Odd numbers between 0 and " + str(limit) + ": ")
displayOddNumbers(limit)
