public class Question4 {
    public static void tri_insertion(int[] l) {
        for (int i = 1; i < l.length; i++) {
            // TODO: Code à compléter
        }
    }

    public static void printArray(int l[]) {
        int n = l.length;
        for (int i = 0; i < n; ++i) {
            System.out.print(l[i] + " ");
        }
    }

    public static void main(String[] args) {
        int[] l = { 2, 43, 1, 3, 43 };
        Question4.tri_insertion(l);
        printArray(l);
    }
}