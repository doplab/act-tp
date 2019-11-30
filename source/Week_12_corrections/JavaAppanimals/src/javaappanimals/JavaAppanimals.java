
package javaappanimals;

/**
 *
 * @author tanjamarkotic inspired by open classroom
 */
public class JavaAppanimals {
// pas possible d'instancier classe abstraite
// mais possible d'instancier un objet Loup mis dans un objet de type Animal

    /**
     * @param args the command line arguments
     */
    
    // méthode main pour tester autres classes
    public static void main(String[] args) {
        // TODO code application logic here
        // instance créé avec mot clé new
        Animal loup = new Loup();
        Chien chien = new Chien();
        Loup l = new Loup("Gris bleuté", 20);
        // appel diverses méthodes:
        loup.manger();
        chien.crier(); 
        l.boire();
        l.manger();
        l.deplacement();
        l.crier();
        // affichage de description loup
        System.out.println(l.toString());
        
    // possible d'appeler Animal.crier() 
    // atout de prog orientée objet = réutilisabilité des objets
    
    // tester polymorphisme d'implémentation:
    //méthodes du chien 
        Chien c = new Chien("Gris bleuté", 20);
        c.boire();
        c.manger();
        c.deplacement();
        c.crier();
        System.out.println(c.toString());	
        System.out.println("--------------------------------------------");
        
    //méthodes de interface
        c.faireCalin();
        c.faireLeBeau();
        c.faireLechouille();
        System.out.println("--------------------------------------------");
        
    //utilisation polymorphisme de interface
        Rintintin r = new Chien();
        r.faireLeBeau();
        r.faireCalin();
        r.faireLechouille();
        
    /* définir deux superclasses pour profiter du polymorphisme!
    interfaces aident à éviter erreurs après chgmt hérarchie! -> encapsulation
        */
    }
}
