import java.util.List;

public class Main {

    public static int recherche_binaire_recursive(List L,int s,int r,int e){  
        //TODO
    }

    public static int plus_proche(List L,int e,int v){  
	//TODO
    }

    public static void main(String[] args) {
        List L = List.of(1,2,5,8,12,16,24,56,58,63);
        int s = 0;
        int r = L.size()-1;
        int e = 64;
        System.out.println(plus_proche(L,e,recherche_binaire_recursive(L,s,r,e)));
        }
    }
