
package javaappanimals;

/**
 *
 * @author tanjamarkotic inspired by open classroom
 */

public abstract class Felin extends Animal {
    // classe abstraite pas « instanciable », mais peut avoir méthodes abstraites
    void deplacement() {
        System.out.println("Je me déplace seul !");
    } 
}