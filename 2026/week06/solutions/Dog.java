import java.util.LinkedList;
import java.util.List;

public class Dog {
    public String name; // Il est préférable de déclarer les attributs comme privés, mais celui-ci est
                        // public pour les buts de l'exercice.
    private List<String> tricks;
    private String race;
    private int age;
    private int mood = 5;
    private static int nbChiens = 0;

    public Dog(String name, List<String> tricks, String race, int age) {
        this.name = name;
        this.race = race;
        this.tricks = tricks;
        this.age = age;
        nbChiens++;
    }
}
