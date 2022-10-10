value1 = 4
value2 = ""

try:
    count = len(value2)
    result= value1/count
except ZeroDivisionError as error:
    print("Nous ne pouvons pas diviser un nombre par 0")
