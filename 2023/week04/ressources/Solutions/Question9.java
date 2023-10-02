public class Question9 {
    public static void division(int a, int b) throws ArithmeticException{
        if(b==0){
            throw new ArithmeticException();
        }else{
            float result = a/b; 
            System.out.println("Le résultat de la division de " + a + "/" + b + "= " + result);
        }
       
    
}
    public static void main(String args[]){
        int value1 = 2;
        int value2 = 4;
        try {
            division(value1,value2);
            value2 = 0;
            division(value1,value2);
        }catch(ArithmeticException err){
            System.out.println("Nous ne pouvons pas effectuer une division par 0");
        }
    }
}
