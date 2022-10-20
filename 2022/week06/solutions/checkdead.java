public static void checkDead() {
    // Initialisation de la liste de Combattants en vie
        List<Combattant> temp = new ArrayList<Combattant>();
        //Ici, on parcourt les instances de Combattant
        for (Combattant f : Combattant.instances) {
            // Et on fait appel à la méthode isAlive() pour vérifier que le Combattant est en vie
            if (f.isAlive()) {
                temp.add(f);
            } else {
                System.out.println(f.getName() + " est mort");
            }
        }
        Combattant.instances = temp;
    }
