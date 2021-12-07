public void attack (String type,Fighter other){
    if(other.isAlive()) {
        int damage = (int)Fighter.attackModifier.get(type) * this.attack - other.getDefense();
        other.setHealth(other.getHealth() - damage);
        Fighter.checkDead();
        Fighter.checkHealth();
    }
    else{
        System.out.println(other.getName() + " est déjà mort");
    }
}
