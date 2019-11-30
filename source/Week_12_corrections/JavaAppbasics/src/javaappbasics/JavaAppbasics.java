package javaappbasics;

import java.util.Scanner;

/**
 *
 * @author tanjamarkotic inspired by openclassroom
 */

public class JavaAppbasics {
// nom de classe avec majuscule par convention
// au minimum une classe pour programme java
    /**
     * @param args the command line arguments
     */
    
    public static void main(String[] args) {
        // TODO code application logic here
        
        // point de départ avec méthode main
        // une seule méthode main par projet 
        System.out.println("Hello! ");
        // saut de ligne à la fin avec println
        System.out.print("My name is ");
        System.out.print(" Webskater!");
        // objet out de classe System
        // JDK pour compilation de programme
        // avec précompilation en byte code
        System.out.println(" What is yours? ");
        Scanner sc = new Scanner(System.in);
        // comme fonction input en python
        String str = sc.nextLine();
        // ou .nextInt()
        System.out.println("Nice to meet you, " + str); 
        
        System.out.println(str + ", you could have a look on the methods"
                + " created in the main class JavaAppbasics! "); 
        
    }
   
    public static void variables (String[] args) {
    // méthodes ajoutées dans classe NewMain doivent être "static"
    // void car pas de return dans méthode
    // ici, programmation orientée objet
    
        int entier = 32;
        float pi = 3.1416f;
        char carac = 'z';
        String mot = "Coucou"; 
        int resultat = 2 + 5;
        System.out.println("Le résultat est = " + resultat);
        int i = 0;
        if (i < 0){
            System.out.println("Ce nombre est négatif !");
        } 
        else {
            if(i == 0)
                // && ou || pour conditions multiples and ou or
                System.out.println("Ce nombre est nul! ");
 
            else
                System.out.println("Ce nombre est positif! ");
 
        }
    }
    
    public static void note (String[] args) {
        int note = 10; 
        // note maximale est 20

        switch (note){
            case 0:
                System.out.println("Ouch!");
                break;
            case 10:
                System.out.println("Vous avez juste la moyenne.");
                break;
            case 20:
                System.out.println("Parfait!");
                break;
            default:
                System.out.println("Il faut davantage travailler.");
        }
        
        int x = 10, y = 20;
        int max = (x < y) ? y : x ; 
        //max vaut maintenant 20
    }
        

    public static void prenom (String[] args){
        
        String prenom;
        //variable prenom vide
        char reponse = 'O';
        //reponse initialisé à O pour oui
        Scanner sc = new Scanner(System.in);
        //objet Scanner avec import de java.util.Scanner 
    
        while (reponse == 'O'){
        //tant que réponse oui … 
            System.out.println("Donnez un prénom : ");
            //instruction
            prenom = sc.nextLine();
            //récupèration prénom saisi par utilisateur
            System.out.println("Bonjour " +prenom+ ", comment vas-tu ?");
            //affichage de la phrase avec le prénom
            System.out.println("Voulez-vous réessayer ? (Oui/Non)");
            //faire un autre essai
            reponse = sc.nextLine().charAt(0);
             //récupèration réponse utilisateur
        }
 
    System.out.println("Au revoir…");
    //fin de la boucle si réponse Non
        
    }
    
   
    public static void tableaux (String[] args){
        int tableauEntier[]= {0,1,2,3,4,5,6,7,8,9};
        int premiersNombres[][] = { {0,2,4,6,8},{1,3,5,7,9} };
    }
}

    

