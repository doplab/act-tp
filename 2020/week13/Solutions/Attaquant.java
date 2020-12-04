class Attaquant extends Combattant{ // a la capacité d attaquer deux fois

    private int multiplicateur;

    public Attaquant(String name, int health, int attack, int defense, int multiplicateur){
        super(name,health,attack,defense);
        this.multiplicateur = multiplicateur;
    }

    public int getMultiplicateur() {
        return multiplicateur;
    }

    public void setMultiplicateur(int multiplicateur){
        this.multiplicateur = multiplicateur;
    }
