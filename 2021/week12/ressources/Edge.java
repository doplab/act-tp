import java.util.List;
import java.util.HashMap;
import java.util.Map;

public class Edge {
    public String from_vertex; // node de départ
    public String to_vertex;  // node d arrivée ( chaîne de caractère)
    public double weight;  // poids de l arête

    public Edge(String from_vertex, String to_vertex, double weight) {
        this.from_vertex = from_vertex;
        this.to_vertex = to_vertex;
        this.weight = weight;
    }

    public void print(){
        Map<String, String> edge_rep = new HashMap <String,String>(); // Création d un dictionnaire pour pouvoir afficher une arête
        edge_rep.put("from_vertex",this.from_vertex);
        edge_rep.put("to_vertex",this.to_vertex);
        edge_rep.put("weight", String.valueOf(this.weight));
        System.out.println(edge_rep);
    }

}