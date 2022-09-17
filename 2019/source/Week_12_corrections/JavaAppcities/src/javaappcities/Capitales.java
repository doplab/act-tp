
package javaappcities;

/**
 *
 * @author tanjamarkotic
 */

/* notion d'héritage
accès aux méthodes public de classe mère, sauf si protected,
méthodes et variables public ou protected utilisés ds classe héritée
*/
public class Capitales extends Villes {

    private String monument;
    //constructeur d'initialisation et  par défaut pour objet Capitales
    public Capitales(){
    /* ce mot clé super appelle le constructeur par défaut de la classe mère  
    et les variables de classe mère dans constructeurs 
    */
        super();
        monument = "aucun";
    }
    // constructeur d'initialisation de capitale avec paramètres
    public Capitales(String nom, int hab, String pays, String monument){
        //même rôle que constructeur par défaut
        super(nom, hab, pays);
        this.monument = monument;
    }  
    
    /* méthode decrisToi() polymorphe: 
    manipulation objet sans connaître type
    possibilité d'appeler la méthode avec Villes ou /et Capitales 
   
    "méthode polymorphe quasi identique à méthode de base, mais se trouve dans 
    une autre classe"
    */
    public String decrisToi(){
        String str =  super.decrisToi() + "\n \t ==>>" 
                + this.monument+ " en est un monument";
        System.out.println("Invocation de super.decrisToi()");
    
        return str;
    }
    //classes héritent méthodes classe Object
    
    // autres infos importantes:
    /* méthode de classe Object souvent redéfinie comme esttoString() retournant 
    String décrivant objet en question (comme decrisToi()). type d'objet pas 
    important pour pouvoir afficher description.... puissance de Java !
    
    redefinition de méthote toString() obligatoire sinon invocation se ferait
    sur classe mère
    */
    
    /* public int hashCode(), attribue hashage à un objet par exemple, pour donner
   id à objet pour catégorisation 
    */
    
    /*classes déclarées final sont immuables, donc pas possible d'hériter 
    objet de classe final! -> pas de redefinition possible si final
    */
}
