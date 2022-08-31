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