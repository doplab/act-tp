package com.company;


import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class Main {

    public static void main(String[] args) {
        List<Integer> ma_liste = List.of(3,2,6,4,1,5);
        HashMap<Integer, String> mon_dictionnaire = new HashMap<Integer, String>(Map.of(1,"un",2,"deux",3,"trois",4,"quatre",5,"cinq",6,"six"));
        System.out.println(ma_liste.get(3));
        System.out.println(ma_liste.get(2));
        System.out.println(mon_dictionnaire.get(ma_liste.get(4)));
        System.out.println(mon_dictionnaire.get(ma_liste.get(0)));
    }
}