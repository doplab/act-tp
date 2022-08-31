public static void checkHealth() {
        for (Fighter f : Fighter.instances) {
            System.out.println(f.getName() + " a encore " + f.getHealth() + " points de vie");
        }
    }
