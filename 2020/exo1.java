// an abstract class declaration\\
public abstract class Animal {
    private int speed;
    // an abstract method declaration
    abstract void run();
}

public class Cat extends Animal {
    // implementation of abstract method
    void run() {
        speed += 10;
    }
}
