public class Main {
    static int a = 0;
    public static void f() {
        a += 2;
        System.out.println("a = " + a);
    }

    public static void g() {
        int b = 3;
        System.out.println("a = " + a);
        System.out.println("b = " + b);
    }

    public static void main(String[] args) {
        f();
        g();
        //System.out.println("b =" + b);
    }
}
