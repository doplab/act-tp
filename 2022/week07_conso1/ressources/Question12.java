public class Question12{
  public static void main(String args[]) {
    try {
      int i  = 7 / 0;
      System.out.print("OUTPUT 1");
    }catch(ArithmeticException e) 
    {
      System.out.print("OUTPUT 2");          
    }
  }
}