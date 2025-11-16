// Solution question 5 - 2/2
    // Fonction principale qui trie arr[l..r] en utilisant
    // merge()
    public static void tri_fusion(int arr[], int l, int r) {
        if (l < r) {
            // Trouver le milieu de la liste
            int m = (l + r) / 2;

            // Trier les première et la deuxième parties de la liste
            tri_fusion(arr, l, m);
            tri_fusion(arr, m + 1, r);

            // Fusionner les deux parties
            merge(arr, l, m, r);
        }
    }

    public static void affiche_liste(int l[]) {
        int n = l.length;
        for (int i = 0; i < n; ++i) {
            System.out.println(l[i] + " ");
        }
    }

    public static void main(String[] args) {
        int[] l = { 38, 27, 43, 3, 9, 82, 10 };
        tri_fusion(l, 0, l.length - 1);
        affiche_liste(l);
    }
}
