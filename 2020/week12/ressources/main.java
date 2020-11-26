public class Main {
    public static void main(String[] args){
        graph test_graph = new graph();
        test_graph.add_vertex("Lausanne");
        test_graph.add_vertex("Geneve");
        test_graph.new_edge("Geneve", "Lausanne", 35);
        test_graph.new_edge("Lausanne", "Berne", 100);
        test_graph.new_edge("Geneve", "Berne", 120);
        test_graph.print();
        test_graph.del_edge("Geneve", "Berne");
        test_graph.print();
    }

}
