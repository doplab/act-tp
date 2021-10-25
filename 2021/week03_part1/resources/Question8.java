public class Main {

    static void raise_error(){
        int variable_1 = 0;
        variable_1 = "Bonjour";
    }

    public static void main(String[] args) {
        if (true) {
            System.out.print("OK");
        }
        else {
            raise_error();
        }
    }
}