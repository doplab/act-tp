package com.company;

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
    private static HashMap<String, Integer> attack_modifier = new HashMap(Map.of("poing", 2, "pied", 2, "tete", 3));


    public Fighter(String name, int health, int attack, int defense) {
        this.name = name;
        this.health = health;
        this.attack = attack;
        this.defense = defense;
        instances.add(this);
    }

        public static void addInstances(Fighter other){
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
            // Initialisation de la liste de Fighter en vie
            List<Fighter> temp = new ArrayList<Fighter>();
            //Ici, on parcourt les instances de Fighter
            for (Fighter f : Fighter.instances) {
                // Et on fait appel à la méthode isAlive() pour vérifier que le Fighter est en vie
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


        public void attack (String type,Fighter other){
            if(other.isAlive()) {
                int damage = (Integer)Fighter.attack_modifier.get(type) * this.attack - other.getDefense();
                other.setHealth(other.getHealth() - damage);
                Fighter.checkDead();
                Fighter.checkHealth();
            }
            else{
                System.out.println(other.getName() + " est déjà mort");
            }
        }
}
