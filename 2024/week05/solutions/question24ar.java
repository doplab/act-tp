public static int fibonacci_r(int n){
        if (n==0 || n==1){
            return n;
        }
        else{
            return fibonacci_r(n-1) + fibonacci_r(n-2);
        }
    }