public class question8 {
    public static void tri_bulle(int[] l) {
        for (int i = 0; i < l.length - 1; i++){
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
        int[] l = {1, 2, 4, 3, 1};
        tri_bulle(l);
        printArray(l);
    }
}