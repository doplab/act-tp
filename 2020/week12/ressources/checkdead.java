public static void checkDead() {
        List<Fighter> temp = new ArrayList<Fighter>();
        for (Fighter f : Fighter.instances) {
            if (f.isAlive()) {
                temp.add(f);
            } else {
                System.out.println(f.getName() + " est mort");
            }
        }
        Fighter.instances = temp;
    }