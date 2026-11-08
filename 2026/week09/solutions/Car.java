class Car extends Vehicle {

    private String modelName = "Mustang";

    public Car(String brand) {
        super(brand);
    }

    public Car(String brand, String modelName) {
        super(brand);
        this.modelName = modelName;
    }

    public String getModelName() {
        return modelName;
    }
}