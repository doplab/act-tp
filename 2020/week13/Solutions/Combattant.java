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
    private static HashMap<String, Integer> attack_modifier = new HashMap(Map.of("poing", 1, "pied", 2, "tete", 3));

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

    public static int getModifier(String type){
        return (int)Combattant.attack_modifier.get(type);
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
    }


    public void attack(String type, Combattant other) {
        if (this.isAlive()) {
            if (other.isAlive()) {
                int damage = (Integer) Combattant.attack_modifier.get(type) * this.attack - other.getDefense();
                other.setHealth(other.getHealth() - damage);
                Combattant.checkDead();
                Combattant.checkHealth();
            } else {
                System.out.println(other.getName() + " est déjà mort");
            }
        }
        else{
            System.out.println(this.getName() +" est mort et ne peut plus rien faire");
        }

    }
}

class Soigneur extends Combattant {

    private int soin;
    private int résurection = 1;

    public Soigneur(String name, int health, int attack, int defense, int soin)
    {
        super(name,health,attack,defense);
        this.soin = soin;
    }

    public int getSoin() {
        return soin;
    }

    public void setSoin(int soin){
        this.soin = soin;
    }

    public int getRésurection(){
        return this.résurection;
    }

    public void setRésurection(int etat){
        this.résurection = etat;
    }
    public void résurection(Combattant other){
        if(this.isAlive()) {
            if (other.isAlive()) {
                System.out.println(other.getName() + " est toujours en vie !");
            } else {
                if (this.getRésurection() == 0) {
                    System.out.println(this.getName() + " ne peut plus ressucite personne");
                } else {
                    other.setHealth(10);
                    Combattant.addInstances(other);
                    this.setRésurection(0);
                    System.out.println(other.getName() + " vient de revenir à la vie");
                }
            }
        }
        else{
            System.out.println(this.getName() +" est mort et ne peut plus rien faire");
        }
    }

    public void soigne(Combattant other) {
        if(this.isAlive()) {
            if (other.getHealth() >= 10) {
                System.out.println(other.getName() + " a déjà le maximum de points de vie");
            }
            if (!other.isAlive()) {
                System.out.println(other.getName() + " est déjà mort, ressucitez le pour pouvoir le soigner");
            } else {
                other.setHealth(other.getHealth() + this.getSoin());
                Combattant.checkHealth();
            }
        }
        else{
            System.out.println(this.getName() +" est mort et ne peut plus rien faire");
        }
    }
}

class Attaquant extends Combattant{

    public Attaquant(String name, int health, int attack, int defense){
        super(name,health,attack,defense);
    }

    public void attack(String type, Combattant other) {
        if (this.isAlive()) {
            if (other.isAlive()) {
                int damage = 2 * (Combattant.getModifier(type) * this.getAttack() - other.getDefense());
                other.setHealth(other.getHealth() - damage);
                Combattant.checkDead();
                Combattant.checkHealth();
            } else {
                System.out.println(other.getName() + " est déjà mort");
            }
        }
        else{
            System.out.println(this.getName() +" est mort et ne peut plus rien faire");
        }

    }


}