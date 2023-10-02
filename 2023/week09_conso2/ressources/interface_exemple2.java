public class Cat extends Animal implements IMakeSound {
    void makeSound(){
        System.out.println("I meow at" + MY_DECIBEL_VALUE + "decibel.");
    }
}
