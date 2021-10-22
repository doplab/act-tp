public static void checkHealth() {
        for (Combattant f : Combattant.instances) {
            System.out.println(f.getName() + " a encore " + f.getHealth() + " points de vie");
        }
    }
