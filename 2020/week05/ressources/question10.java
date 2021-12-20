public class question10 {
    public static void tri_insertion(int[] l) {
        for (int i = 1; i < l.length; i++){
            //TODO: Code à compléter 
        }
    }
    
    public static void printArray(int l[]){ 
        int n = l.length; 
        for (int i = 0; i < n; ++i) 
            System.out.print(l[i] + " "); 
        System.out.println(); 
    } 

    
    public static void main(String[] args){
        int[] l = {2, 43, 1, 3, 43};
        tri_insertion(l);
        printArray(l);
    }
}