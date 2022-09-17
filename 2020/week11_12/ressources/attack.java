public void attack (String type,Combattant other){
            if(other.isAlive()) {
                int damage = (Integer)Combattant.attack_modifier.get(type) * this.attack - other.getDefense();
                other.setHealth(other.getHealth() - damage);
                Combattant.checkDead();
                Combattant.checkHealth();
            }
            else{
                System.out.println(other.getName() + " est déjà mort");
            }
