
package javaappcities;

/**
 *
 * @author tanjamarkotic
 */

// public class pour pouvoir être appelée de n'importe quel file du projet
public class Villes {
// méthodes private appelées que depuis l'intérieur de la classe où elle se trouve
/* variables d'instance publics pour définir caractéristiques d'objets
 ou private pr que ces attributs ne sont plus accessibles en dehors de la classe 
 où ils sont déclarés
 */
    protected String nomVille;
    protected String nomPays;
    protected int nbreHabitants; 
    protected char categorie;
     
    //variable publique pour compter les instances
    public static int nbreInstances = 0;

    //variable privée pour compter les instances avec accesseurs
    protected static int nbreInstancesBis = 0;        
  
    /* constructeur par défaut sans aucun paramètre: 
    méthode d'instance pour créer ou instancier des objets et initialiser 
    variables de classe communes à toutes les instances de votre classe /
    constructeur comme méthode avec aucun type de retour (ni void, ni double)/
    même nom que classe!!
    */
    public Villes(){
    //incrémentation nbreInstances à chaque appel aux constructeurs
        nbreInstances++;
        nbreInstancesBis++;   
        
    // system.out.println
    // préciser cas si aucune valeur donnée 
        System.out.println("Création d'une ville !");      
        nomVille = "Inconnu";
        nomPays = "Inconnu";
        nbreHabitants = 0;
        this.setCategorie();
  } 
    
    /* constructeur avec paramètres:
    « p » en première lettre des paramètres ajouté pour mieux les repérer
    */
    public Villes(String pNom, int pNbre, String pPays){
    //incrémentation nbreInstances à chaque appel aux constructeurs
        nbreInstances++;
        nbreInstancesBis++;   
        
    // system.out.println
    // préciser cas si aucune valeur donnée 
        System.out.println("Création d'une ville avec des paramètres !");
        nomVille = pNom;
        nomPays = pPays;
        nbreHabitants = pNbre;
        this.setCategorie();
    }  
       
    /* ------ ACCESSEURS get -------
    méthodes pour accéder ou afficher aux variables des objets,
    public pour y accéder depuis classe main,
    même type que variable devant être retournée
    */
    // retourne  nom ville
    public String getNom(){  
        return nomVille;
    }

    // retourne nom pays
    public String getNomPays(){
        return nomPays;
    }

    // retourne nombre d'habitants
    public int getNombreHabitants(){
        return nbreHabitants;
    } 
    
    // retourne catégorie ville
    public char getCategorie(){
        return categorie;
    }
    
    // retourne nbre Instances en static
    public static int getNombreInstancesBis(){
        return nbreInstancesBis;
    }  
 
    /* ------ MUTATEURS set  -------
    méthode pour accéder  ou modifier variables des objets 
    type void car retourne aucune valeur mais fait mise à jour
    */

    //définit nom ville
    public void setNom(String pNom){
        nomVille = pNom;
    }

    //définit nom pays
    public void setNomPays(String pPays){
        nomPays = pPays;
    }

    //définit nombre d'habitants
    public void setNombreHabitants(int nbre){
        nbreHabitants = nbre;
        this.setCategorie();
    } 
    
    
    //définit catégorie sans paramètre, sans renvoi car màj auto même si modif nbrehab
    private void setCategorie() {
 
        // création nouvelles bornes et catégorie
        int bornesSuperieures[] = {0, 1000, 10000, 100000, 500000, 1000000, 5000000, 10000000};
        char categories[] = {'?', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H'};

        // petites règles pour définir catégorie
        int i = 0;
        while (i < bornesSuperieures.length && this.nbreHabitants > bornesSuperieures[i])
            i++;
            this.categorie = categories[i];
    /* this fait référence à l'objet courant pour désigner une de ses variables 
    ou une de ses méthodes comme self en python
    */
    }

    //retourne description de ville en objet de type string
    public String decrisToi(){
        return "\t"+this.nomVille+" est une ville de "
                +this.nomPays+ ", elle comporte : "
                +this.nbreHabitants+" habitant(s) => elle est donc de catégorie: "
                +this.categorie;
    }

    //retourne chaîne de caractères selon résultat de comparaison
    public String comparer(Villes v1){
        /* si méthode appelée dans main avec v.comparer(v2), 
        v est l'exécutant et doit trouver un moyen de appeler ses propres données
        ->this
        */
        String str = new String();
        
        if (v1.getNombreHabitants() > this.nbreHabitants)
            str = v1.getNom()+" est une ville plus peuplée que "+this.nomVille;
     
        else
            str = this.nomVille+" est une ville plus peuplée que "+v1.getNom();
     
        return str;
    }
    
    
 /* "Ici, un objet dont les variables sont protégées de l'extérieur a été créé.
 En effet, depuis l'extérieur de la classe, elles ne sont accessibles que
 via les accesseurs et mutateurs définis. C'est le principe d'encapsulation! " 
 */
  
}


