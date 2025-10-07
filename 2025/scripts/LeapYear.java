public class LeapYear {
    static boolean isLeap(int year) {
        return (year % 4 == 0) && (year % 100 != 0) || (year % 400 == 0);
    }

    static void reportLeapYear(int year) {
        boolean leap = isLeap(year);
        System.out.println("isLeap(" + year + ")=" + leap);
    }

    public static void main(String[] args) {
        int year = 2000;
        reportLeapYear(year);
    }
}
