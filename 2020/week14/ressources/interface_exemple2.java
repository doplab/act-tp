
public class Cat extends Animal implements IMakesound {

    void makesound(){
        System.out.println("I meow at" + MY_DECIBEL_VALUE + "decibel.");
    }
}
