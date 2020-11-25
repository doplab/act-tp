import java.util.List;
import java.util.HashMap;
import java.util.Vector;

public class graph_empty {

    // Les attributs de la class graph
    public List<Edges> edges = new Vector();   // Utilisation de vector car il faut que l'on puisse rajouter ou supprimer des éléments de la liste
    public List<String> vertices = new Vector();



    // Methode qui permet l'ajout d'un sommet au graph.
    public void add_vertex(String name){
        this.vertices.add(name); // Méthode qui permet d'ajouter un sommet au graph
    }

    // Cette méthode va tester si le sommet demandé existe dans le graph. Si oui retourne le poids, sinon retourne 0.
    public double edge_exist(String from_vertex, String to_vertex){
        // Ecrire votre code ci-dessous

        


        // Fin de la zone d'écriture
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
        // Ecrire votre code ci-dessous






        // Fin de la zone d'écriture
    }
    // Méthode qui va ajouter l'arête dans le graph.
    public void new_edge(String from_vertex, String to_vertex, double weight){
        // Ecrire votre code ci-dessous












        // Fin de la zone d'écriture
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

    // Fonction qui permet d'imprimer les composants d'un graph
    public void print(){
        for(int i=0; i< this.vertices.size(); ++i){
            System.out.println("The vertex number " + (i+1) + " has a value of: " + this.vertices.get(i));
        }
        for (Edges edge : this.edges){
            edge.print();
        }
    }
}

