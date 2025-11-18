public class Lasagna {
    public int expectedMinutesInOven() {
        return 40;
    }
    
    public int remainingMinutesInOven(int inOven) {
        return 40 - inOven;
    }

    public int preparationTimeInMinutes(int layers) {
        return 2 * layers;
    }

    public int totalTimeInMinutes(int layers, int inOven) {
        return (2 * layers) + inOven;
    }
}
