class Soigneur extends Fighter {

    private int resurrection;

    public Soigneur(String name, int health, int attack, int defense, int soin) {
        super(name, health, attack, defense);
        this.resurrection = 1;
    }

    public int getResurrection() {
        return this.resurrection;
    }

    public void setResurrection(int etat) {
        this.resurrection = etat;
    }
}