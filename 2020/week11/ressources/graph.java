public class graph {
    // Les attributs de la class graphe
    public List<Edge> edges = new Vector();   // "Utilisation de vector car il faut que l'on puisse rajouter ou supprimer des éléments de la liste"
    public List<String> vertices = new Vector();



    // "Méthode qui permet l'ajout d'un sommet au graphe."
    public void add_vertex(String name){
        this.vertices.add(name); // "Méthode qui permet d'ajouter un sommet au graphe"
    }

    // "Cette méthode va tester si le sommet demandé existe dans le graphe. Si oui retourne le poids, sinon retourne 0."
    public double edge_exist(String from_vertex, String to_vertex){
        for (Edge edge : this.edges) {
            if (edge.from_vertex == from_vertex & edge.to_vertex == to_vertex) {
                return edge.weight;
            }
        }
        return 0;
    }
    // "L'implémentation de la méthode ci dessous n'est pas importante pour vous à comprendre. Elle vous est utile pour"
    // "générer une arête lorsque vous cherchez à en ajouter une à votre graphe. Elle fait aussi le test si jamais"
    // "les sommets utilisés font partis du graphe ou non. Si non, elle va les ajouter au graphe. Cette méthode peut"
    // "être utile dans la méthode new_edge"
    private void generate_edge(String from_vertex, String to_vertex, double weight){
        if (this.vertices.contains(from_vertex) & this.vertices.contains(to_vertex)){
            Edge new_edge = new Edges(from_vertex,to_vertex,weight);
            this.edges.add(new_edge);
        }
        else {
            if (!this.vertices.contains(from_vertex)){
                this.vertices.add(from_vertex);
            }
            if (!this.vertices.contains(to_vertex)){
                this.vertices.add(to_vertex);
            }
            Edge new_edge = new Edge(from_vertex,to_vertex,weight);
            this.edges.add(new_edge);
        }

    }

}
