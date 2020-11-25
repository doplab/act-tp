public void attack (Fighter other){
            if(other.isAlive()) {
                int damage = this.attack - other.getDefense();
                other.setHealth(other.getHealth() - damage);
                Fighter.checkDead();
                Fighter.checkHealth();
                System.out.println("-------------");
            }
            else{
                System.out.println(other.getName() + " est déjà mort");
                System.out.println("-------------");
            }
        }