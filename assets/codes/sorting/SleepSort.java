public class SleepSort {
    public static void sleepSort(int[] arr) {
        for (final int n : arr) {
            new Thread(() -> {
                try {
                    Thread.sleep(n);
                } catch (InterruptedException e) {
                    Thread.currentThread().interrupt();
                }
                System.out.print(n + " ");
            }).start();
        }
        try {
            Thread.sleep(1000);
        } catch (InterruptedException e) {
            Thread.currentThread().interrupt();
        }
        System.out.println();
    }

    public static void main(String[] args) {
        int[] data = {40, 70, 20, 90, 30, 80, 20};
        sleepSort(data);
    }
}
