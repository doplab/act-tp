class Soup extends Food implements Drinkable {
    public Soup(String name, double price, ArrayList<String> ingredients) {
        super(name, price, ingredients);
    }

    public void drinkMe() {
        System.out.println("Drink the soup !" + this.toString());
        // ou System.out.println("Drink the soup !" + this);
    }
}
