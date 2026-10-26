jours_semaine = {1:"lundi", 2:"mardi", 3:"mercredi", 4:"jeudi", 5:"jeudi", 6:"samedi"} 
jours_semaine[5] = "vendredi"
jours_semaine[7] = "dimanche"
print(jours_semaine[3])
liste_jours = [jours_semaine[x] for x in jours_semaine if x % 2 == 0] 
