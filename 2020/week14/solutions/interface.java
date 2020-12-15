import java.util*;


public interface Edible{
    void eatMe();
}
public interface Drinkable{
    void drinkMe();
}
public class Food extends Item implements Edible{
    public Food (String name, double price, ArrayList<String> ingredients){
        super(name, price, ingredients);
    }
    public void eatMe(){
        System.out.println("Eat me!" + toString());
    }
}

public class Soup extends Food implements Drinkable{
    public Soup(String name, double price, ArrayList<String> ingredients){
        super(name, price, ingredients);
    }
    public void drinkMe(){
        System.out.println("Drink the soup !" + toString());
    }
}

