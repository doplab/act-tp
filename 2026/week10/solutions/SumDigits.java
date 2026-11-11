public class SumDigits {
    public static int sumDigits(int number) {
        if (number == 0) {
            return 0;
        } else {
            return (number % 10) + sumDigits(number / 10);
        }
    }

    public static void main(String[] args) {
        System.out.println(sumDigits(126));
    }
}