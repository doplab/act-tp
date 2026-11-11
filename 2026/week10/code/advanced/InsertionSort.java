public class InsertionSort {
    public static void triInsertion(int[] l) {
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
        InsertionSort.triInsertion(l);
        printArray(l);
    }
}