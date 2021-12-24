class Graph {
    // Attributs de la class graph
    public List<Edge> edges = new Vector();   // Utilisation de vector car il faut que l on puisse rajouter ou supprimer des éléments de la liste
    public List<String> vertices = new Vector();

    // Méthode qui permet l ajout d un sommet au graph.
    public void addVertex(String name){
        this.vertices.add(name); // Méthode qui permet d ajouter un sommet au graph
    }

    // Cette méthode va tester si le sommet demandé existe dans le graph. Si oui retourne le poids, sinon retourne 0.
    public double edgeExist(String fromVertex, String toVertex){
        for (Edge edge : this.edges) {
            if (edge.fromVertex == fromVertex & edge.toVertex == toVertex) {
                return edge.weight;
            }
        }
        return 0;
    }
    // Cette méthode permet de générer une arête lorsque vous cherchez à en ajouter une à votre graphe. Elle fait aussi le test si jamais les sommets utilisés font partis du graphe ou non. Si non, elle va les ajouter au graphe. Cette méthode peut être utile dans la méthode newEdge
    private void generateEdge(String fromVertex, String toVertex, double weight){
        if (this.vertices.contains(fromVertex) & this.vertices.contains(toVertex)){
            Edge newEdge = new Edge(fromVertex,toVertex,weight);
            this.edges.add(newEdge);
        }
        else {
            if (!this.vertices.contains(fromVertex)){
                this.vertices.add(fromVertex);
            }
            if (!this.vertices.contains(toVertex)){
                this.vertices.add(toVertex);
            }
            Edge newEdge = new Edge(fromVertex,toVertex,weight);
            this.edges.add(newEdge);
        }
    }

    public void updateWeight(String fromVertex, String toVertex, double weight){
        for (Edge edge : this.edges){
            if(edge.fromVertex == fromVertex & edge.toVertex == toVertex){
                edge.weight = weight;
                System.out.println("Weight of" + edge + "has been updated");
            }
            else {
                System.out.println("The vertex between the two nodes given does not exist, it will be created.");
            }
        }
    }

    // Méthode nous permettant de supprimer une arête du graph.
    public void delEdge(String fromVertex, String toVertex){
        for( Edge edge : this.edges ){
            if (edge.fromVertex == fromVertex & edge.toVertex == toVertex){
                this.edges.remove(edge);
                System.out.println("Edge between " + fromVertex + " and " + toVertex + " has been deleted.");
                break;
            }
        }
    }
 
