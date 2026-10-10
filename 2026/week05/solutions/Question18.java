import java.util.HashMap;
import java.util.Map;

public class Question18 {

    public static void main(String[] args) {
        HashMap<String, Integer> monDictionnaire = new HashMap<String, Integer>(
                Map.of("étudiants", 14000, "enseignants", 2300, "collaborateurs", 0));
        System.out.println(monDictionnaire.get("étudiants"));
        int tailleDictionnaire = monDictionnaire.size();
        System.out.println(tailleDictionnaire);
        monDictionnaire.put("collaborateurs", 950);
        monDictionnaire.put("pays", 86);
        for (String key : monDictionnaire.keySet()) {
            System.out.println(key + " : " + monDictionnaire.get(key));
        }
    }
}