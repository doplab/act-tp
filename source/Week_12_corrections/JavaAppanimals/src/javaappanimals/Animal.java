
package javaappanimals;

/**
 *
 * @author tanjamarkotic inspired by open classroom
 */

/* classes abstaites pour définir superclasse 
enfants utilisent attributs et méthodes public ou protected de superclasse,
méthode abstraite existe que dans classe abstraite
*/
abstract class Animal{
    // classes enfants obligées de redéfinir méthodes de superclasse,
    /* 2 constructeurs pour classes enfants : par défaut et avec paramètres
    d'initialisation.*/
     
    protected String couleur;
    protected int poids;

    protected void manger(){
        System.out.println("Je mange de la viande.");
    }  
    protected void boire(){
        System.out.println("Je bois de l'eau !");
    }
    
    // méthodes abstraites sans corps 
    abstract void deplacement();
        
    abstract void crier();
        
    @Override
    public String toString(){
        String str = "Je suis un objet de la " + this.getClass() + ", je suis "
                + this.couleur + ", je pèse " + this.poids;
        return str;
        
    /* Dans méthode toString() de classe Animal, utilisation 
    méthode getClass() pour retourner nom de classe */
    

    // héritage multiple interdit en Java
    
    /* développer nouveau supertype et s'en servir dans classe Chien
    ->  interfaces pour créer un nouveau supertype,
    possible ajout infini d'interfaces dans une seule classe !
     interface = classe 100 % abstraite !
    */
    }   
}