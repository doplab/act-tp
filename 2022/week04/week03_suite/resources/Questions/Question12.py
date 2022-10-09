teacher = "Garbinato"
assistant = "Diallo"
lesson = "ACT"

if ((teacher == "Diallo") or not(teacher == "Garbinato")) and (lesson == "ACT"):
    print("Alpha Diallo et Benoît Garbinato")
elif ((teacher == "Benfares") and (lesson == "ACT")) or (teacher == assistant):
    print("Anass Benfares")
elif (teacher == "Gaelle" or assistant == "Diallo") and (lesson == "ACT" and teacher == "Julien"):
    print("Gaelle Barillère")
elif ((teacher == "Garbinato" or lesson == "INF") and assistant == "Diallo") or (lesson == "ACT" or teacher == "Hafsa"):
    print(teacher + " : Professeur du cours Algorithmique et pensée computationelle.")
else:
    print("Benoît")