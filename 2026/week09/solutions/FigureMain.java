class FigureMain {
    public static void main(String[] args) {
        Carre c = new Carre(5.0f);
        Rectangle r = new Rectangle(4.0f, 3.0f);
        System.out.println(c.getPerimetre());
        System.out.println(r.getAire());
    }
}