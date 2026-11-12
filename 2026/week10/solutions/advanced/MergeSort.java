public class MergeSort {
    // Fusionne 2 sous-listes de arr[].
    // Première sous-liste est arr[l..m]
    // Deuxième sous-liste est arr[m+1..r]
    public static void merge(int arr[], int l, int m, int r) {
        // Trouver la taille des deux sous-listes à fusionner
        int n1 = m - l + 1;
        int n2 = r - m;

        /* Créer des listes temporaires */
        int leftArray[] = new int[n1];
        int rightArray[] = new int[n2];

        /* Copier les données dans les sous-listes temporaires */
        for (int i = 0; i < n1; ++i) {
            leftArray[i] = arr[l + i];
        }
        for (int j = 0; j < n2; ++j) {
            rightArray[j] = arr[m + 1 + j];
        }

        /* Fusionner les sous-listes temporaires */
        // Indexes initiaux de la première et seconde sous-liste
        int i = 0, j = 0;

        // Index initial de la sous-liste fusionnée
        int k = l;
        while (i < n1 && j < n2) {
            if (leftArray[i] <= rightArray[j]) {
                arr[k] = leftArray[i];
                i++;
            } else {
                arr[k] = rightArray[j];
                j++;
            }
            k++;
        }

        /* Copier les élements restants de leftArray[] */
        while (i < n1) {
            arr[k] = leftArray[i];
            i++;
            k++;
        }

        /* Copier les élements restants de rightArray[] */
        while (j < n2) {
            arr[k] = rightArray[j];
            j++;
            k++;
        }
    }

    // Fonction principale qui trie arr[l..r] en utilisant
    // merge()
    public static void triFusion(int arr[], int l, int r) {
        if (l < r) {
            // Trouver le milieu de la liste
            int m = (l + r) / 2;

            // Trier les première et la deuxième parties de la liste
            triFusion(arr, l, m);
            triFusion(arr, m + 1, r);

            // Fusionner les deux parties
            merge(arr, l, m, r);
        }
    }

    public static void afficheListe(int l[]) {
        int n = l.length;
        for (int i = 0; i < n; ++i) {
            System.out.println(l[i] + " ");
        }
    }

    public static void main(String[] args) {
        int[] l = { 38, 27, 43, 3, 9, 82, 10 };
        triFusion(l, 0, l.length - 1);
        afficheListe(l);
    }
}
