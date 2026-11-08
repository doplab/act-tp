import java.util.*;

public class Food extends Item implements Edible {
    public Food(String name, double price, List<String> ingredients) {
        super(name, price, ingredients);
    }

    @Override
    public void eatMe() {
        System.out.println("Eat me!" + toString());
    }
}
