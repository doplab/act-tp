import com.sun.tools.corba.se.idl.constExpr.Not;

public class question_conso1_mergesort {
    // Fusionne 2 sous-listes de arr[].
    // Première sous-liste est arr[l..m]
    // Deuxième sous-liste est arr[m+1..r]
    public static int[] merge(int[] arr1, int[] arr2) {
        // Trouver la taille des deux sous-listes à fusionner
        int n1 = arr1.length;
        int n2 = arr2.length;
        /* Créer des listes temporaires */
        int L[] = new int[n1];
        int R[] = new int[n2];
        int F[] = new int[n1 + n2];
        /*Copier les données dans les sous-listes temporaires */
        for (int i = 0; i < n1; ++i) {
            L[i] = arr1[i];
        }
        for (int j = 0; j < n2; ++j) {
            R[j] = arr2[j];
        }
        /* Fusionner les sous-listes temporaires */
        // Indexes initiaux de la première et seconde sous-liste
        int i = 0, j = 0;
        // Index initial de la sous-liste fusionnée
        int k = 0;
        // Boucle qui fusionne L et R de manière ordonnée
        while (i < n1 && j < n2) {

            if (L[i] <= R[j]) {
                F[k] = L[i];
                i++;
                ++k;
            } else {
                F[k] = R[j];
                j++;
                ++k;
            }
        }
        // On rajoute les valeurs qui ne sont pas encore ajoutées dans F
        while (i < n1 || j < n2) {
            if (i < n1) {
                F[k] = L[i];
                ++i;
                ++k;
            } else {
                F[k] = R[j];
                ++j;
                ++k;
            }
        }

        return F;
    }
    public static void affiche_liste(int l[]) {
        int n = l.length;
        for (int i = 0; i < n; ++i)
            System.out.print(l[i] + " ");
    }
    public static void main(String[] args) {
        int[] l1 = {3, 10, 12};
        int[] l2 = {5, 7, 14, 15};
        int[] l = merge(l1, l2);
        affiche_liste(l);

    }
}
