public void attack(String type, Fighter other) {
        for (int i = 0; i < this.getMultiplicateur(); i++) {
            System.out.println("Attaque n " + (i+1));
            super.attack(type, other);
        }
    }