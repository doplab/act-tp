teacher = "Benoît"
assistant = "Bob"
lesson = "ACT"

if ((teacher == "Bob") or not(teacher == "Benoît")) and (lesson == "ACT"):
    print("Benoît et Bob")
elif ((teacher == "Charlie") and (lesson == "ACT")) or (teacher == assistant):
    print("Charlie")
elif (teacher == "David" or assistant == "Bob") and (lesson == "ACT" and teacher == "Eve"):
    print("Eve")
elif ((teacher == "Benoît" or lesson == "INF") and assistant == "Bob") or (lesson == "ACT" or teacher == "Sam"):
    print(teacher + " : Professeur du cours d'Algorithmes et Pensée Computationnelle.")
else:
    print("Alice")
