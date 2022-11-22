public class question {
    public static int sum_digits(int number) {
        if(number == 0){
            return 0;
        } else{
            return (number%10) + sum_digits(number/10);
        }
    }

    public static void main(String[] args){
        System.out.println(sum_digits(126));
    }
}