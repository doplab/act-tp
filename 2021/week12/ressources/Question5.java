public String get_oldest(Dog other) {
    if (other.getAge() < this.getAge()){
        return this.name + " est le chien le plus agé avec " + this.age + " ans";
    }
    else{
        return other.name + " est le chien le plus agé avec " + other.getAge() + " ans";
    }
}