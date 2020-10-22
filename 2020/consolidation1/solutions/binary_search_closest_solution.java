package com.company;
import java.util.List;

public class Main {

    public static int recherche_binaire_recursive(List L,int s,int r,int e){  // fonction 1, recherche binaire
        if (s<=r){
            int mid = (s+r)/2;
            int element = (int) L.get(mid);
            if (element == e){
                return mid;
            }
            if(element > e){
                return recherche_binaire_recursive(L,s,mid-1,e);
            }
            else {
                return recherche_binaire_recursive(L,mid+1,r,e);
            }
        }
        else{
            int mid = (s+r)/2;
            return mid;
        }
    }

    public static int plus_proche(List L,int e,int v){  //fonction 2, comparaison pour trouver l'élément le plus proche

        if (v==L.size()-1){  // si l'élément retourné par la première fonction est le dernier élément de la liste,
            if (Math.abs((int) L.get(v-1)-e) < Math.abs((int) L.get(v)-e)){ // il n'a pas besoin de comparer avec l'élément suivant
                return (int) L.get(v-1);
            }
            else {
                return (int) L.get(v);
            }
        }

        else if (v==0){ // si l'élément retourné par la première fonction est le premier élément de la liste,
            if (Math.abs((int) L.get(v+1)-e) < Math.abs((int) L.get(v)-e)){ // il n'a pas besoin de comparer avec l'élément d'avant
                return (int) L.get(v+1);
            }
            else {
                return (int) L.get(v);
            }
        }

        else{ // cas normal
            if (Math.abs((int) L.get(v-1)-e) < Math.abs((int) L.get(v)-e)){
                return (int) L.get(v-1);
            }
            else if (Math.abs((int) L.get(v+1)-e) < Math.abs((int) L.get(v)-e)){
                return (int) L.get(v+1);
            }
            else {
                return (int) L.get(v);
            }
        }
    }
    public static void main(String[] args) {
        List L = List.of(1,2,5,8,12,16,24,56,58,63);
        int s = 0;
        int r = L.size()-1;
        int e = 64;
        System.out.println(plus_proche(L,e,recherche_binaire_recursive(L,s,r,e)));
        }
    }