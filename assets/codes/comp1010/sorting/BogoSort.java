public class BogoSort {
    public static void bogoSort(int[] arr) {
        java.util.Random rnd = new java.util.Random();
        int best = countInOrder(arr);
        System.out.println("Initial sortedness: " + best);
        while (best < arr.length) {
            for (int i = 0; i < arr.length; i++) {
                int j = rnd.nextInt(arr.length);
                int temp = arr[i];
                arr[i] = arr[j];
                arr[j] = temp;
            }
            int current = countInOrder(arr);
            if (current > best) {
                best = current;
                System.out.println("New record: " + best);
            }
        }
    }

    private static int countInOrder(int[] arr) {
        if (arr.length == 0) {
            return 0;
        }
        int count = 1;
        for (int i = 1; i < arr.length; i++) {
            if (arr[i] >= arr[i - 1]) {
                count++;
            }
        }
        return count;
    }

    public static void main(String[] args) {
        int[] data = {40, 70, 20, 90, 30, 80, 20};
        bogoSort(data);
        for (int n : data) {
            System.out.print(n + " ");
        }
        System.out.println();
    }
}
