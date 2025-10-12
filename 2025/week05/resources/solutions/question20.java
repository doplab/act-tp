public static int factoriel(int x){
        if (x == 0){
            return 1;
        }
        else{
            return x*factoriel(x-1);
        }
    }
    public static void main(String[] args) {
        System.out.println(factoriel(5));
    }