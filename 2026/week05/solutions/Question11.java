import java.util.ArrayList;
import java.util.Arrays;
import java.util.Iterator;
import java.util.List;

class Question11 {
    public static void main(String[] args) {
        List<Integer> nombres = new ArrayList<>(Arrays.asList(1, 2, 3, 4, 5, 6, 7, 8, 9, 10));
        Iterator<Integer> iter = nombres.iterator();
        
        while(iter.hasNext()){
            if (iter.next()%2==1){
                iter.remove();
            }
        }
        System.out.println(nombres);
    }
}