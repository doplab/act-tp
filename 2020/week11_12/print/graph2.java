
    // Méthode qui va ajouter l arête dans le graph.
    public void new_edge(String from_vertex, String to_vertex, double weight){
        double test_existence = this.edge_exist(from_vertex,to_vertex); // Peut valoir soit le point de l arête soit 0 si elle n existe pas.
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
        for( Edge edge : this.edges ){
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
        for (Edge edge : this.edges){
            edge.print();
        }
    }
}