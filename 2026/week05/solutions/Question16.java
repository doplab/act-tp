import java.util.HashMap;
import java.util.Map;

public class Question16 {

    public static void main(String[] args) {
        HashMap<String, Integer> monDictionnaire = new HashMap<String, Integer>(
                Map.of("etudiants", 14000, "enseignants", 2300, "collaborateurs", 0));
        System.out.println(monDictionnaire.get("etudiants"));
        int tailleDictionnaire = monDictionnaire.size();
        System.out.println(tailleDictionnaire);
        monDictionnaire.put("collaborateurs", 950);
        monDictionnaire.put("pays", 86);
        for (String key : monDictionnaire.keySet()) {
            System.out.println(key + " : " + monDictionnaire.get(key));
        }
    }
}