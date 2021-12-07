import java.util.List;
import java.util.HashMap;
import java.util.Map;
import java.util.Vector;

class Edge {
    public String fromVertex; // node de départ
    public String toVertex;  // node d arrivée (chaîne de caractère)
    public double weight;  // poids de l arête

    public Edge(String fromVertex, String toVertex, double weight) {
        this.fromVertex = fromVertex;
        this.toVertex = toVertex;
        this.weight = weight;
    }

    public void print(){
        Map<String, String> edgeRep = new HashMap <String,String>(); // Création d un dictionnaire pour pouvoir afficher une arête
        edgeRep.put("From Vertex",this.fromVertex);
        edgeRep.put("To Vertex",this.toVertex);
        edgeRep.put("Weight", String.valueOf(this.weight));
        System.out.println(edgeRep);
    }
}