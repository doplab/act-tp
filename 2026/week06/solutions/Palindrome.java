public class Palindrome {
    public static void main(String[] args) {
        String pal1 = "abba";
        String pal2 = "ata";
        String nonPal1 = "abca";
        System.out.println(isPalindrome(pal1));
        System.out.println(isPalindrome(pal2));
        System.out.println(isPalindrome(nonPal1));
    }

    public static boolean isPalindrome(String text) {
        int length = text.length();
        if (length == 1 || length == 0) {
            return true;
        }
        return text.charAt(0) == text.charAt(length - 1)
                && isPalindrome(text.substring(1, length - 1));
    }
}
