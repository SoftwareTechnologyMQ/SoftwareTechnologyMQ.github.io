public class RadixSort {
    public static void radixSort(int[] arr) {
        int max = arr[0];
        for (int i = 1; i < arr.length; i++) {
            if (arr[i] > max) {
                max = arr[i];
            }
        }
        int exp = 1;
        int[] aux = new int[arr.length];
        while (max / exp > 0) {
            int[] count = new int[10];
            for (int n : arr) {
                count[(n / exp) % 10]++;
            }
            for (int i = 1; i < 10; i++) {
                count[i] += count[i - 1];
            }
            for (int i = arr.length - 1; i >= 0; i--) {
                int digit = (arr[i] / exp) % 10;
                aux[count[digit] - 1] = arr[i];
                count[digit]--;
            }
            System.arraycopy(aux, 0, arr, 0, arr.length);
            exp *= 10;
        }
    }

    public static void main(String[] args) {
        int[] data = {40, 70, 20, 90, 30, 80, 20};
        radixSort(data);
        for (int n : data) {
            System.out.print(n + " ");
        }
        System.out.println();
    }
}
