public class Main {

    static double aire(int rayon){
        return Math.pow(rayon, 2)*Math.PI;
    }

    static double perimetre(int rayon){
        return 2*Math.PI*rayon;
    }

    public static void main(String[] args) {
        int rayon = 5;
        double aire = aire(rayon);
        double perimetre = perimetre(rayon);
        System.out.println("L'aire d'un cercle de rayon "+rayon+" est égale à "+aire);
        System.out.println("Le périmètre d'un cercle de rayon "+rayon+" est égal à "+perimetre);
    }
}