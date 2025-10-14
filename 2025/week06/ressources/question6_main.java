public class Main {
    public static void main(String[] args) {
        Dog lola = new Dog("Lola",List.of("rollover"),"Bouvier",10);
        Dog tobi = new Dog("Tobi",List.of("rollover","do a barrel"),"Doggo",17);
        System.out.println(lola.getAge());
        System.out.println(lola.getMood());
        System.out.println(lola.getRace());
        System.out.println(lola.name);
        System.out.println(lola.getTricks());
        lola.setAge(13);
        lola.setMood(8);
        lola.setRace("Bouvier");
        lola.name = "lola";
        lola.setTricks(List.of("rollover","do a barrel"));
        lola.eat();
        lola.leash();
        lola.addTrick("sit");
        System.out.println(Dog.getNbChiens());
        System.out.println(lola.getOldest(tobi));
        System.out.println(lola);
    }
}