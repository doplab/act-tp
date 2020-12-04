import java.util.HashMap;
import java.util.List;
import java.util.ArrayList;
import java.util.Map;

public class Combattant {
    private String name;
    private int health;
    private int attack;
    private int defense;
    private static List<Combattant> instances = new ArrayList<Combattant>();
    private static HashMap<String, Integer> attack_modifier = new HashMap(Map.of("poing", 2, "pied", 2, "tete", 3));

    public Combattant(String name, int health, int attack, int defense) {
        this.name = name;
        this.health = health;
        this.attack = attack;
        this.defense = defense;
        instances.add(this);
    }

    public static void addInstances(Combattant other){
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
        this.health = health;
    }

    public void setName(String name) {
        this.name = name;
    }

    public Boolean isAlive() {
        if (this.health > 0) {
            return true;
        } else {
            return false;
        }
    }

    public static void checkDead() {
        // Initialisation de la liste de Combattants en vie
        List<Combattant> temp = new ArrayList<Combattant>();
        //Ici, on parcourt les instances de Combattant
        for (Combattant f : Combattant.instances) {
            // Et on fait appel à la méthode isAlive() pour vérifier que le Combattant est en vie
            if (f.isAlive()) {
                temp.add(f);
            } else {
                System.out.println(f.getName() + " est mort");
            }
        }
        Combattant.instances = temp;
    }


    public static void checkHealth() {
        for (Combattant f : Combattant.instances) {
            System.out.println(f.getName() + " a encore " + f.getHealth() + " points de vie");
        }
        System.out.println("------------------------------");
    }


    public void attack(String type, Combattant other) {
        if (!this.isAlive()) {
            System.out.println(this.getName() + " est mort et ne peut plus rien faire");
        }
        else{
            if (!other.isAlive()) {
                System.out.println(other.getName() + " est déjà mort");
            }
            else{
                int damage = (int) Combattant.attack_modifier.get(type) * this.attack - other.getDefense();
                other.setHealth(other.getHealth() - damage);
                Combattant.checkDead();
                Combattant.checkHealth();
            }
        }

    }
}

class Soigneur extends Combattant { 

    //TODO 

    public Soigneur(String name, int health, int attack, int defense, int soin)
    {
        //TODO
    }

    //TODO


    public void résurrection(Combattant other){
        //TODO
    }

    public void attack(Combattant other) {
        //TODO
    }
}

class Attaquant extends Combattant{ // a la capacité d'attaquer deux fois

    //TODO

    public Attaquant(String name, int health, int attack, int defense, int multiplicateur){
      	//TODO
    }

    //TODO

    public void attack(String type, Combattant other) {
        //TODO
    }
}