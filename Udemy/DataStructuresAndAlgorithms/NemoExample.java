import java.util.Arrays;

class NemoExample {
    public static void main(String[] args) {
        String[] nemo = {"nemo"};

        String[] everyone = {"dory", "bruce", "marlin", "nemo", "gill", "bloat", "nigel", "squirt", "darla", "hank"};

        String[] bigArray = new String[100];

        Arrays.fill(bigArray, "nemo");

        for (int i = 0; i < bigArray.length; i++) {
            System.out.println(bigArray[i]);
        }
    }
}