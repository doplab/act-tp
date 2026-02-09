public class Question6Recursive{
    public static int fibonacci_r(int n){
        if (n==0 || n==1){
            return n;
        }
        else{
            return fibonacci_r(n-1) + fibonacci_r(n-2);
        }
    }
    public static void main(String[] args) {
        System.out.println(fibonacci_r(10));
    }
}