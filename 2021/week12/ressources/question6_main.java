public class Main {
    public static void main(String[] args) {
        Dog Lola = new Dog("Loola",List.of("rollover"),"Bouviier",10);
        Dog Tobi = new Dog("Tobi",List.of("rollover","do a barrel"),"Doggo",17);
        System.out.println(Lola.getAge());
        System.out.println(Lola.getMood());
        System.out.println(Lola.getRace());
        System.out.println(Lola.name);
        System.out.println(Lola.getTricks());
        Lola.setAge(13);
        Lola.setMood(8);
        Lola.setRace("Bouvier");
        Lola.name = "Lola";
        Lola.setTricks(List.of("rollover","do a barrel"));
        Lola.eat();
        Lola.leash();
        Lola.add_trick("sit");
        System.out.println(Dog.getNb_chiens());
        System.out.println(Lola.get_oldest(Tobi));
        System.out.println(Lola);
    }
}