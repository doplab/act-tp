public class Main {
    public static class Vehicle {
        protected String brand;

        public Vehicle(String brand) {
            this.brand = brand;
        }

        public void honk() {
            System.out.println("Tuut, tuut!");
        }
    }
    public static class Car extends Vehicle{

        public String modelName = "Mustang";
        public Car(String brand) {
            super(brand);
        }
    }

    public static void main(String[] args) {
        Car myCar = new Car("Ford");
        myCar.honk();
        System.out.println(myCar.brand + " "+myCar.modelName);
    }
}
