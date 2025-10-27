package com.company;

class Soigneur extends Fighter {

    private int resurrection;

    public Soigneur(String name, int health, int attack, int defense, int soin){
        super(name,health,attack,defense);
        resurrection = 1;
    }

    public int getResurrection(){
        return this.resurrection;
    }

    public void setResurrection(int etat){
        this.resurrection = etat;
    }

    public void resurrection(Fighter other){
        if(!this.isAlive()) {
            System.out.println(this.getName() + " est mort et ne peut plus rien faire");
            return;
        }
        if (other.isAlive()) {
            System.out.println(other.getName() + " est toujours en vie !");
            return;
        } 
        if (this.getResurrection() == 0) {
            System.out.println(this.getName() + " ne peut plus ressuciter personne");
            return;
        }
        other.setHealth(10);
        Fighter.addInstances(other);
        this.setResurrection(0);
        System.out.println(other.getName() + " vient de revenir à la vie");
        Fighter.checkHealth();
    }

    public void attack(Fighter other) {
        if(!this.isAlive()) {
            System.out.println(this.getName() + " est mort et ne peut plus rien faire");
        }
        else{
            if (other.getHealth() >= 10) {
                System.out.println(other.getName() + " a déjà le maximum de points de vie");
            }
            if (!other.isAlive()) {
                System.out.println(other.getName() + " est déjà mort, ressuscitez-le pour pouvoir le soigner");
            } else {
                other.setHealth(other.getHealth() + this.getAttack());
                Fighter.checkHealth();
            }
        }
    }

}