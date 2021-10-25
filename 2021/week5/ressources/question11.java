public class question11 {
    // Fusionne 2 sous-listes de arr[]. 
    // Première sous-liste est arr[l..m] 
    // Deuxième sous-liste est arr[m+1..r] 
    public static void merge(int arr[], int l, int m, int r) {
        // TODO: Code à compléter 
    }
    
    // Fonction principale qui trie arr[l..r] en utilisant 
    // merge() 
    public static void tri_fusion(int arr[], int l, int r){
        // TODO: Code à compléter 
    }
    
    public static void printArray(int l[]){ 
        int n = l.length; 
        for (int i = 0; i < n; ++i) 
            System.out.print(l[i] + " "); 
  
        System.out.println(); 
    } 

    
    public static void main(String[] args){
        int[] l = {38, 27, 43, 3, 9, 82, 10};
        tri_fusion(l, 0, l.length - 1);
        printArray(l);
    }
}