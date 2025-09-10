import java.util.HashMap;
import java.util.Map;

public class Main {

    public static void main(String[] args) {
        HashMap<String, Integer> mon_dictionnaire = new HashMap<String, Integer>(Map.of("étudiants", 14000, "enseignants", 2300, "collaborateurs", 0));
        System.out.println(mon_dictionnaire.get("étudiants"));
        int taille_dictionnaire = mon_dictionnaire.size();
        System.out.println(taille_dictionnaire);
        mon_dictionnaire.put("collaborateurs", 950);
        mon_dictionnaire.put("pays", 86);
        for (String keys : mon_dictionnaire.keySet()) {
            System.out.println(keys + " : " + mon_dictionnaire.get(keys));
        }
    }
}