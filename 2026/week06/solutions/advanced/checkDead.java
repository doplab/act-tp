public static void checkDead() {
    // Initialisation de la liste de Fighter en vie
        List<Fighter> temp = new ArrayList<Fighter>();
        //Ici, on parcourt les instances de Fighter
        for (Fighter f : Fighter.instances) {
            // Et on fait appel à la méthode isAlive() pour vérifier que le Fighter est en vie
            if (f.isAlive()) {
                temp.add(f);
            } else {
                System.out.println(f.getName() + " est mort");
            }
        }
        Fighter.instances = temp;
    }