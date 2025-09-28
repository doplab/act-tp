public class Question15 {
    public static void main(String[] args) {
        String s = "School of Criminal Sciences\nUNIL";

        System.out.println(s); // \n creates a newline

        // 2. Print only the substring "School of Criminal Sciences"
        System.out.println(s.substring(0, 27));

        // 3. Access the third character
        System.out.println(s.charAt(2)); // 'h'
    }
}
