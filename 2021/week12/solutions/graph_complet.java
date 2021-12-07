package com.company;

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

public class Main {
    public static void main(String[] args){
        Graph test_graph = new Graph();
        test_graph.addVertex("Lausanne");
        test_graph.addVertex("Geneve");
        test_graph.newEdge("Geneve", "Lausanne", 35);
        test_graph.newEdge("Lausanne", "Berne", 100);
        test_graph.newEdge("Geneve", "Berne", 120);
        test_graph.print();
        test_graph.delEdge("Geneve", "Berne");
        test_graph.print();
    }
}