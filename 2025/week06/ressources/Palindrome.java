public class Palindrome {
    public static void main(String[] args) {
        String pal1 = "abba";
        String pal2 = "ata";
        String nonpal1 = "abca";
        System.out.println(isPalindrome(pal1));
        System.out.println(isPalindrome(pal2));
        System.out.println(isPalindrome(nonpal1));
    }

    public static boolean isPalindrome(String palindrome) {
        int length = palindrome.length();
        if (length == 1 || length == 0) {
            return true;
        }
        return palindrome.charAt(0) == palindrome.charAt(length - 1)
                && isPalindrome(palindrome.substring(1, length - 1));
    }
}
