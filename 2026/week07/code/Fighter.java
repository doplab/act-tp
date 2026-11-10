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
    private static HashMap<String, Integer> attackModifier = new HashMap<String, Integer>(
            Map.of("poing", 2, "pied", 2, "tete", 3));

    public Fighter(String name, int health, int attack, int defense) {
        this.name = name;
        this.setHealth(health);
        this.attack = attack;
        this.defense = defense;
        instances.add(this);
    }

    // Réinscrit un combattant ressuscité dans la liste des combattants en vie.
    public static void addInstance(Fighter other) {
        instances.add(other);
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
        if (health < 0) {
            this.health = 0;
        } else if (health > 10) {
            this.health = 10;
        } else {
            this.health = health;
        }
    }

    public void setName(String name) {
        this.name = name;
    }

    public boolean isAlive() {
        return this.health > 0;
    }

    public static void checkDead() {
        List<Fighter> temp = new ArrayList<Fighter>();
        for (Fighter f : Fighter.instances) {
            if (f.isAlive()) {
                temp.add(f);
            } else {
                System.out.println(f.getName() + " est mort");
            }
        }
        Fighter.instances = temp;
    }

    public static void checkHealth() {
        for (Fighter f : Fighter.instances) {
            System.out.println(f.getName() + " a encore " + f.getHealth() + " points de vie");
        }
        System.out.println("------------------------------");
    }

    public void attack(String type, Fighter other) {
        if (other.isAlive()) {
            int damage = Fighter.attackModifier.get(type) * this.attack - other.getDefense();
            if (damage < 0) {
                damage = 0;
            }
            other.setHealth(other.getHealth() - damage);
            Fighter.checkDead();
            Fighter.checkHealth();
        } else {
            System.out.println(other.getName() + " est déjà mort");
        }
    }
}
