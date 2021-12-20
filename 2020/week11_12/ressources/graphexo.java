import java.util.List;
import java.util.HashMap;
import java.util.Vector;

public class graph {

    // Les attributs de la class graph
    public List<Edges> edges = new Vector();   // Utilisation de vector car il faut que l'on puisse rajouter ou supprimer des éléments de la liste
    public List<String> vertices = new Vector();



    // Methode qui permet l'ajout d'un sommet au graph.
    public void add_vertex(String name){
        this.vertices.add(name); // Méthode qui permet d'ajouter un sommet au graph
    }

    // Cette méthode va tester si le sommet demandé existe dans le graph. Si oui retourne le poids, sinon retourne 0.
    public double edge_exist(String from_vertex, String to_vertex){
        for (Edges edge : this.edges) {
            if (edge.from_vertex == from_vertex & edge.to_vertex == to_vertex) {
                return edge.weight;
            }
        }
        return 0;
    }
    // L'implémentation de la méthode ci dessous n'est pas importante pour vous à comprendre. Elle vous est utile pour
    // générer une arête lorsque vous cherchez à en ajouter une à votre graph. Elle fait aussi le test si jamais
    // les sommets utilisés font partis du graph ou non. Si non, elle va les ajouter au graph. Cette méthode peut
    // être utile dans la méthode new_edge
    private void generate_edge(String from_vertex, String to_vertex, double weight){
        if (this.vertices.contains(from_vertex) & this.vertices.contains(to_vertex)){
            Edges new_edge = new Edges(from_vertex,to_vertex,weight);
            this.edges.add(new_edge);
            }
        else {
            if (!this.vertices.contains(from_vertex)){
                this.vertices.add(from_vertex);
            }
            if (!this.vertices.contains(to_vertex)){
                this.vertices.add(to_vertex);
            }
            Edges new_edge = new Edges(from_vertex,to_vertex,weight);
            this.edges.add(new_edge);
        }

        }

    public void update_weight(String from_vertex, String to_vertex, double weight){
        for (Edges edge : this.edges){
            if(edge.from_vertex == from_vertex & edge.to_vertex == to_vertex){
                edge.weight = weight;
                System.out.println("Weight of" + edge + "has been updated");
            }
            else {
                System.out.println("The vertex between the two nodes given does not exist, it will be created.");
            }
        }

    }
    // Méthode qui va ajouter l'arête dans le graph.
    public void new_edge(String from_vertex, String to_vertex, double weight){
        double test_existence = this.edge_exist(from_vertex,to_vertex); // Peut valoir soit le point de l'arête soit 0 si elle n'existe pas.
        if ( test_existence == weight){
            System.out.println("Edge between" + from_vertex + " and " + to_vertex + " with the same weight already exists");
        }
        else{
            if ( test_existence != 0) {
                System.out.println("Edge between" + from_vertex + " and " + to_vertex + "exists but with a different weight and will be overwritten");
                this.update_weight(from_vertex, to_vertex, weight);
            }
            else{
                this.generate_edge(from_vertex, to_vertex, weight);
            }
        }

    }

    // Méthode nous permettant de supprimer une arête du graph.
    public void del_edge(String from_vertex, String to_vertex){
        for( Edges edge : this.edges ){
            if (edge.from_vertex == from_vertex & edge.to_vertex == to_vertex){
                this.edges.remove(edge);
                System.out.println("Edge between " + from_vertex + " and " + to_vertex + " has been deleted.");
                break;
            }

        }

    }

    public void print(){
        for(int i=0; i< this.vertices.size(); ++i){
            System.out.println("The vertex number " + (i+1) + " has a value of: " + this.vertices.get(i));
        }
        for (Edges edge : this.edges){
            edge.print();
        }
    }
}



