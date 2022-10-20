public class Dog {
    public String name;
    private List tricks;
    private String race;
    private int age;
    private int mood = 5;
    private static int nb_chiens = 0;

    public Dog(String name, List tricks, String race, int age) {
        this.name = name;
        this.race = race;
        this.tricks = tricks;
        this.age = age;
        nb_chiens++;
    }

}
