
package javaappcities;

/**
 *
 * @author tanjamarkotic inspired by openclassroom
 */
public class JavaAppcities {
    // nom de classe avec majuscule
    // au minimum une classe pour programme java
    // point de départ avec main méthode
    /**
     * @param args the command line arguments
     */
    // contexte static: la méthode main.
    public static void main(String[] args) {
        // TODO code application logic here
        // 3 différentes manières d'instancier des objets:
        Villes ville1;
        ville1 = new Villes("Ollon", 6910, "Suisse ");
        
        Villes v0 = new Villes();
        
        Villes v1 = new Villes("Rougement", 1659, "Suisse ");  
        
        Villes v2 = new Villes("Genève", 495249, "Suisse ");
        
        // utilisation de system.out.println comme print en python:
        System.out.println("\n v = "+v0.getNom()+" ville de  "
                +v0.getNombreHabitants()+ " habitants se situant en "
                +v0.getNomPays());
        System.out.println(" v1 = "+v1.getNom()+" ville de  "
                +v1.getNombreHabitants()+ " habitants se situant en "
                +v1.getNomPays());
        System.out.println(" v2 = "+v2.getNom()+" ville de  "
                +v2.getNombreHabitants()+ " habitants se situant à "
                +v2.getNomPays()+"\n\n");
        
        // interchanger les noms des villes avec leurs mutateurs:
        v1.setNom("Champex-Lac ");
        v2.setNom("Tanay ");
        // utilisation de system.out.println comme print en python:
        System.out.println(" v1 = "+v1.getNom()+" ville de  "
                +v1.getNombreHabitants()+ " habitants se situant en "
                +v1.getNomPays());
        System.out.println(" v2 = "+v2.getNom()+" ville de  "
                +v2.getNombreHabitants()+ " habitants se situant en "
                +v2.getNomPays()+"\n\n");
        
        //system.out.println pour voir resultat méthode decris toi:
        System.out.println("\n\n"+v1.decrisToi());
        System.out.println(v0.decrisToi());
        System.out.println(v2.decrisToi()+"\n\n");
        
        //system.out.println pour voir resultat méthode comparer:
        System.out.println(v1.comparer(v2));
        System.out.println(v2.comparer(v1));
        
        //system.out.println pour voir resultat méthode
        // getNombreInstancesBis() de classes villes:
        System.out.println("Le nombre d'instances de la classe Ville est : "
                + Villes.getNombreInstancesBis());
        
        // instancier nouvelle objet Capitales
        Capitales cap = new Capitales();
        System.out.println(cap.decrisToi());
        
        // instancier nouvelle objet Capitales
        Capitales cap1;
        cap1 = new Capitales("Montreux ", 20000, "Suisse", "Freddy Mercury ");
        System.out.println("\n"+cap1.decrisToi());
       
    }
    
}
