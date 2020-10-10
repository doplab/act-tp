// Solution question 9 - 2/2
public static void affiche_liste(int l[]) {
    int n = l.length;
    for (int i = 0; i < n; ++i)
        System.out.println(l[i] + " ");
}


public static void main(String[] args) {
    int[] l = {38, 27, 43, 3, 9, 82, 10};
    tri_fusion(l, 0, l.length - 1);
    affiche_liste(l);
}
}