public class Question3 {
    public static void main(String[] args) {

        int nbBonbons = 11;
        int nbPersonnes = 3;
        nbBonbons ++;
        nbPersonnes --;
        int bonbonsPersonnes = nbBonbons / nbPersonnes;
        int reste = nbBonbons % nbPersonnes;
        System.out.println(nbBonbons);
        System.out.println(nbPersonnes);
        System.out.println(bonbonsPersonnes);
        System.out.println(reste);
    }
}
