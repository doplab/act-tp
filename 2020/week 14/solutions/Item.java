package com.company;
import java.util.*;


public abstract class Item {

    private int id;
    private static int count = 0;
    private String name;
    private double price;
    private ArrayList<String> ingredients;

    public Item (String name, double price, ArrayList<String> ingredients) {
        this.id = ++count;
        this.name = name;
        this.price = price;
        this.ingredients = ingredients;
    }

    public int getID() {
        return this.id;
    }

    public String getName() {
        return this.name;
    }

    public double getPrice() {
        return this.price;
    }

    public ArrayList<String> getIngredients() {
        return this.ingredients;
    }

    public boolean equals(Object o) {
        if (o instanceof Item) {
            Item i = (Item) o;
            return i.getID() == this.getID();
        }
        return false;
    }

    public String toString() {
        return "*-*-*-*-*-*" +
                "\nID: " + this.getID() +
                "\nName: " + this.getName() +
                "\nPrice: " + this.getPrice() + " CHF" +
                "\nList of ingredients: " + this.getIngredients().toString() +
                "\n*-*-*-*-*-*";
    }
}