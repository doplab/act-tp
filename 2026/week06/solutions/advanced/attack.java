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
