class FigureMain {
    public static void main(String[] args) {
        Carre c = new Carre(5.0);
        Rectangle r = new Rectangle(4.0, 3.0);
        System.out.println(c.getPerimetre());
        System.out.println(r.getAire());
    }
}