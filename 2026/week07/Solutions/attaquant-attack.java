public void attack(String type, Fighter other) {
    if (!this.isAlive()) {
        System.out.println(this.getName() + " est mort et ne peut plus rien faire");
        return;
    }
    for (int i = 0; i < this.getMultiplicateur(); i++) {
        System.out.println("Attaque n " + (i + 1));
        super.attack(type, other);
    }
}
