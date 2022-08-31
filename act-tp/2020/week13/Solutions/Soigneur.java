class Soigneur extends Fighter { 

    private int résurrection;

    public Soigneur(String name, int health, int attack, int defense, int soin)
    {
        super(name,health,attack,defense);
        résurrection = 1;
    }

    public int getRésurrection(){
        return this.résurrection;
    }

    public void setRésurrection(int etat){
        this.résurrection = etat;
    }