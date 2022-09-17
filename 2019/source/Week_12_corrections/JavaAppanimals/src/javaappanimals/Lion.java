
package javaappanimals;

/**
 *
 * @author tanjamarkotic inspired by open classroom
 */

public class Lion extends Felin {
 
    public Lion(){
    }

    public Lion(String couleur, int poids){
        this.couleur = couleur;
        this.poids = poids;
    }       
 
    void crier() {
        System.out.println("Je rugis dans la savane !");
    } 
}
