public void résurrection(Fighter other){
    if(!this.isAlive()) {
        System.out.println(this.getName() + " est mort et ne peut plus rien faire");
    }
    else{
        if (other.isAlive()) {
            System.out.println(other.getName() + " est toujours en vie !");
        } else {
            if (this.getRésurrection() == 0) {
                System.out.println(this.getName() + " ne peut plus ressuciter personne");
            } else {
                other.setHealth(10);
                Fighter.addInstances(other);
                this.setRésurrection(0);
                System.out.println(other.getName() + " vient de revenir à la vie");
                Fighter.checkHealth();
            }
        }
    }
}
