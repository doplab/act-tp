    public void print(){
        for(int i=0; i< this.vertices.size(); ++i){
            System.out.println("The vertex number " + (i+1) + " has a value of: " + this.vertices.get(i));
        }
        for (Edge edge : this.edges){
            edge.print();
        }
    }
    // "Méthode qui va ajouter l'arête dans le graph."
    public void newEdge(String fromVertex, String toVertex, double weight){
        double testExistence = this.edgeExist(fromVertex,toVertex); // Peut valoir soit le point de l'arête soit 0 si elle n'existe pas.
        if (testExistence == weight){
            System.out.println("Edge between" + fromVertex + " and " + toVertex + " with the same weight already exists");
        }
        else{
            if (testExistence != 0) {
                System.out.println("Edge between" + fromVertex + " and " + toVertex + "exists but with a different weight and will be overwritten");
                this.updateWeight(fromVertex, toVertex, weight);
            }
            else{
                this.generateEdge(fromVertex, toVertex, weight);
            }
        }
    }
}