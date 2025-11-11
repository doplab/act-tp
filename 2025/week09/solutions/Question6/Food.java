import java.util.*;

public class Food extends Item implements Edible {
    public Food(String name, double price, ArrayList<String> ingredients) {
        super(name, price, ingredients);
    }

    public void eatMe() {
        System.out.println("Eat me!" + toString());
    }
}

class Soup extends Food implements Drinkable {
    public Soup(String name, double price, ArrayList<String> ingredients) {
        super(name, price, ingredients);
    }

    public void drinkMe() {
        System.out.println("Drink the soup !" + this.toString());
        // ou System.out.println("Drink the soup !" + this);
    }
}
