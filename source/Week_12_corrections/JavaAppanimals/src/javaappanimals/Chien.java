
package javaappanimals;

/**
 *
 * @author tanjamarkotic inspired by open classroom
 */

// implémentation interface dans classe Chien
public class Chien extends Canin implements Rintintin {
    // constructeurs par défaut et avec paramètres
    public Chien(){
    }

    public Chien(String couleur, int poids){
        this.couleur = couleur;
        this.poids = poids;
    }       

    @Override
    public void crier() {
        System.out.println("J'aboie sans raison !");
    } 
    /* ordre déclarations primordial car expression d'héritage avant expression 
    d'implémentation, sinon code ne compilera pas.
    */
    
    public void faireCalin() {
        System.out.println("Je te fais un GROS CÂLIN");               
    }

    public void faireLeBeau() {
        System.out.println("Je fais le beau !");
    }

    public void faireLechouille() {
        System.out.println("Je fais de grosses léchouilles...");
    } 
    
}