Scanner sc = new Scanner(System.in);
System.out.println("Veuillez entrer l'âge de la personne : ");
int age = sc.nextInt();
if(age<21){
	System.out.println("Entrée : Pas OK");
        }
else{
   	if(age>25){
              	System.out.println("Entrée : OK, Boisson : Pas OK");
            }
       	else{
             	System.out.println("Entrée : OK, Boisson : OK");
            }
        }