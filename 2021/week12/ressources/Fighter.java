import java.util.HashMap;
import java.util.List;
import java.util.ArrayList;
import java.util.Map;

public class Fighter {
    private String name;
    private int health;
    private int attack;
    private int defense;
    private static List<Fighter> instances = new ArrayList<Fighter>();
    private static HashMap<String, Integer> attackModifier = new HashMap(Map.of("poing",1,"pied",2,"tete",3));

    public Fighter(String name, int health, int attack, int defense) {
        this.name = name;
        this.health = health;
        this.attack = attack;
        this.defense = defense;
        instances.add(this);
    }

    public int getAttack() {
        return attack;
    }

    public int getHealth() {
        return health;
    }

    public int getDefense() {
        return defense;
    }

    public String getName() {
        return name;
    }

    public void setAttack(int attack) {
        this.attack = attack;
    }

    public void setDefense(int defense) {
        this.defense = defense;
    }

    public void setHealth(int health) {
        this.health = health;
    }

    public void setName(String name) {
        this.name = name;
    }

    public Boolean isAlive() {
        // à compléter
    }

    public static void checkDead() {
        // à compléter
    }

    public static void checkHealth() {
        // à compléter
    }

    public void attack (String type, Fighter other){
        // à compléter
    }
}

