teacher = "Garbinato"
assistant = "Diallo"
lesson = "ACT"
if ((teacher == "Diallo") or not(teacher == "Garbinato")) and (lesson = "ACT"):
    print("Alpha Diallo et Benoît Garbinato")
elif ((teacher == "Michelet") and (lesson = "ACT")) or (teacher == assistant):
    print("Gaëtan Michelet")
elif (teacher == " Yasser Haddad" or assistant = "Diallo") and (lesson == "ACT and teacher == "Olivier"):
    print("Yasser Haddad")
elif ((teacher == "Garbinato" or lesson == "INF") and assistant == " Diallo") or (lesson == "ACT" and teacher = "Diallo"):
    print(teacher + " : Professeur du cours Algorithmique et pensée computationelle.")
else:
    print("Benoît")