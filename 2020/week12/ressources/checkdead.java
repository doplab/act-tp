public static void checkDead() {
        List<Combattant> temp = new ArrayList<Combattant>();
        for (Combattant f : Combattant.instances) {
            if (f.isAlive()) {
                temp.add(f);
            } else {
                System.out.println(f.getName() + " est mort");
            }
        }
        Combattant.instances = temp;
    }
