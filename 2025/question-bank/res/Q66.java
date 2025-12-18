// Solution possible
public boolean canPlay(Cat otherCat) {
    if (this.mood < 3 || otherCat.getMood() < 3) {
        return false;
    } else {
        return true;
    }
}
