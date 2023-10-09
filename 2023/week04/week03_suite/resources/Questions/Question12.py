teacher = "Garbinato"
assistant = "Diallo"
lesson = "ACT"

if ((teacher == "Diallo") or not(teacher == "Garbinato")) and (lesson == "ACT"):
    print("Alpha Diallo et Benoît Garbinato")
elif ((teacher == "George") and (lesson == "ACT")) or (teacher == assistant):
    print("Amaury George")
elif (teacher == "Mathieu" or assistant == "Diallo") and (lesson == "ACT" and teacher == "Marc"):
    print("Marc Pitteloud")
elif ((teacher == "Garbinato" or lesson == "INF") and assistant == "Diallo") or (lesson == "ACT" or teacher == "Valentin"):
    print(teacher + " : Professeur du cours d'Algorithmes et Pensée Computationnelle.")
else:
    print("Benoît")