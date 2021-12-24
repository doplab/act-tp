import java.util.List;
import java.util.HashMap;
import java.util.Vector;

public class graph_empty {

    // Les attributs de la classe graphe
    public List<Edge> edges = new Vector();   // Utilisation de Cector car il faut que l on puisse rajouter ou supprimer des éléments de la liste
    public List<String> vertices = new Vector();
    
    // Méthode qui permet l ajout d un sommet au graphe.
    public void addVertex(String name){
        this.vertices.add(name); // Méthode qui permet d ajouter un sommet au graphe
    }

    // Cette méthode va tester si le sommet demandé existe dans le graphe. Si oui retourne le poids, sinon retourne 0.

    public double edgeExist(String from_vertex, String toVertex){

        // Ecrire votre code ici

    }
    
    // La méthode ci-dessous vous permet de générer une arête lorsque vous cherchez à en ajouter une à votre graphe. Elle fait aussi le test si jamais les sommets utilisés font partis du graphe ou non. Si non, elle va les ajouter au graphe. Cette méthode peut être utile dans la méthode new_edge

    private void generate_edge(String from_vertex, String toVertex, double weight){
        if (this.vertices.contains(from_vertex) & this.vertices.contains(toVertex)){
            Edge new_edge = new Edge(from_vertex,toVertex,weight);
            this.edges.add(new_edge);
        }
        else {
            if (!this.vertices.contains(from_vertex)){
                this.vertices.add(from_vertex);
            }
            if (!this.vertices.contains(toVertex)){
                this.vertices.add(toVertex);
            }
            Edge new_edge = new Edge(from_vertex,toVertex,weight);
            this.edges.add(new_edge);
        }

    }

    public void updateWeight(String from_vertex, String toVertex, double weight){
        // Ecrire votre code ici
    }
    // Méthode qui va ajouter l arête dans le graphe.
    public void new_edge(String from_vertex, String toVertex, double weight){
        // Ecrire votre code ici
    }

    // Méthode nous permettant de supprimer une arête du graphe.
    public void delEdge(String from_vertex, String toVertex){
        for(Edge edge : this.edges ){
            if (edge.from_vertex == from_vertex & edge.toVertex == toVertex){
                this.edges.remove(edge);
                System.out.println("Edge between " + from_vertex + " and " + toVertex + " has been deleted.");
                break;
            }
        }
    }

    // Fonction qui permet d imprimer les composants d un graphe
    public void print(){
        for(int i=0; i< this.vertices.size(); ++i){
            System.out.println("The vertex number " + (i+1) + " has a value of: " + this.vertices.get(i));
        }
        for (Edge edge : this.edges){
            edge.print();
        }
    }
}

