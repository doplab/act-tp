public String getOldest(Dog other) {
    if (other.getAge() < this.getAge()){
        return this.name + " est le chien le plus âgé : il a " + this.age + " ans";
    }
    else{
        return other.name + " est le chien le plus âgé : il a " + other.getAge() + " ans";
    }
}
