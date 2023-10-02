a = 2.0
b = 5
c = "hello world"

if type(a) == int:
    print("output 1")
if (type(a) == int or type(c) == str) and b!=2.0:
    print("output 2")
if (a*b >= 10 or type(c) == bool) and type(a) == float:
    print("output 3")
