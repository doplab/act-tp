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