public class Question6Iterative{

    public static int fibonacci_i(int n){
        if (n==0 || n==1){
            return n;
        }
        else{
            int old_fib = 1;
            int new_fib = 1;
            int tmp;
            for (int i=2; i<n; i++){
                tmp = new_fib;
                new_fib = new_fib+old_fib;
                old_fib = tmp;
            }
            return new_fib;
        }
    }
    public static void main(String[] args){
        System.out.println(fibonacci_i(10));
    }
}