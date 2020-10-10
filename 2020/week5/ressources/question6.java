public class Main {
                        public static void tri_bulle(int[] l) {
                            for (int i = 0; i < l.length - 1; i++){
                                for (int j = 0; j < n-i-1; j++) {
                                    if (l[j] > l[j+1]) { 
                                        // échange l[j+1] et l[i] 
                                        int temp = l[j]; 
                                        l[j] = l[j+1]; 
                                        l[j+1] = temp; 
                                    } 
                            }
                        }
                        
                        public static void printArray(int l[]){ 
                            int n = l.length; 
                            for (int i = 0; i < n; ++i) 
                                System.out.print(arr[i] + " "); 
                      
                            System.out.println(); 
                        } 
              
                        
                        public static void main(String[] args){
                            int[] l = {1, 2, 4, 3, 1};
                            tri_bulle(l);
                            printArray(l);
                        }
                    }