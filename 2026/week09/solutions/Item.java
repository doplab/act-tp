import java.util.*;

public abstract class Item {

    private int id;
    private static int count = 0;
    private String name;
    private double price;
    private List<String> ingredients;

    public Item(String name, double price, List<String> ingredients) {
        this.id = ++count;
        this.name = name;
        this.price = price;
        this.ingredients = ingredients;
    }

    public int getId() {
        return this.id;
    }

    public String getName() {
        return this.name;
    }

    public double getPrice() {
        return this.price;
    }

    public List<String> getIngredients() {
        return this.ingredients;
    }

    @Override
    public boolean equals(Object o) {
        if (o instanceof Item) {
            Item i = (Item) o;
            return i.getId() == this.getId();
        }
        return false;
    }

    @Override
    public String toString() {
        return "ID: " + this.id +
                "\nName: " + this.name +
                "\nPrice: " + this.price + " CHF" +
                "\nList of ingredients: " + this.ingredients;
    }
}
