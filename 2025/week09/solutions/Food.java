import java.util.*;

public class Food extends Item implements Edible {
    public Food(String name, double price, ArrayList<String> ingredients) {
        super(name, price, ingredients);
    }

    public void eatMe() {
        System.out.println("Eat me!" + toString());
    }
}

