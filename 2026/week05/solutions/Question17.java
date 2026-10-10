import java.util.List;
import java.util.LinkedList;

public class Question17 {

    public static void main(String[] args) {
        List maListe = List.of(1, 2, 3, 4);
        System.out.println(maListe.get(1));
        System.out.println(maListe.size());
        LinkedList maListeM = new LinkedList(maListe);
        maListeM.addFirst(0);
        maListeM.addLast(6);
        for (int i = 0; i < maListeM.size(); i++) {
            System.out.println(maListeM.get(i));
        }
    }
}
