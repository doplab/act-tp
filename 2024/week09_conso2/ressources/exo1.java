// Exemple de classe abstraite
public abstract class Animal {
    private int speed;
    // Déclaration d une méthode abstraite
    abstract void run();
}

public class Cat extends Animal {
        // Implémentation d une méthode abstraite
        void run() {
            speed += 10;
        }
