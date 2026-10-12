public void attack (String type, Fighter other){
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
