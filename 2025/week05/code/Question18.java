import java.util.ArrayList;
import java.util.Arrays;
import java.util.Iterator;
import java.util.List;

class Question18 {
    public static void main(String[] args) {
        List<Integer> nombres = new ArrayList<>();
        for (int i  =0; i < 11; i++){
            nombres.add(i);
        }
        Iterator<Integer> iter = nombres.iterator();
        
        while(iter.hasNext()){
            if (iter.next()%2==1){
                iter.remove();
            }
        }
        System.out.println(nombres);
    }
}