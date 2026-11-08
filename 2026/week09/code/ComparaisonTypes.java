public class ComparaisonTypes {
    public static void main(String[] args) {
        Figure rectangle = new Rectangle(4.0, 3.0);
        Figure carre = new Carre(5.0);

        System.out.println(rectangle instanceof Carre);
        System.out.println(carre instanceof Rectangle);
        System.out.println(carre instanceof Figure);
        System.out.println(carre.getClass() == Rectangle.class);
        System.out.println(carre.getClass() == Carre.class);
    }
}
