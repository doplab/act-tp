import sys

match input():
    case "/var/www/./public/..":
        print("index.html")
    case "/var/www/src/..":
        print("index.html")
    case "/var/www/src/":
        print("Main.class\nMain.java")
    case "/var/www/public/":
        print("esc.png")
    case _: print("La saisie n'était pas reconnue")