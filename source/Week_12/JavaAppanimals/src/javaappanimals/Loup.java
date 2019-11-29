
package javaappanimals;

/**
 *
 * @author tanjamarkotic inspired by open classroom
 */


public class Loup extends Canin {
 
    public Loup(){            
    }

    public Loup(String couleur, int poids){
        this.couleur = couleur;
        this.poids = poids;
    }       
 
    void crier() {
        System.out.println("Je hurle à la Lune en faisant ouhouh !"); 
    }
}