/**
 * Demonstrates the dual-pivot variant of quick sort.
 *
 * <p>This implementation mirrors the style of the other example sorts in this
 * repository but includes extra commentary so the control flow is easy to
 * follow in lecture slides.  The algorithm partitions the array using two
 * pivots, resulting in three sub arrays which are then sorted recursively.</p>
 */
public class DoublePivotQuickSort {

    /**
     * Sorts {@code arr[low..high]} using dual-pivot quick sort.
     *
     * @param arr  the array to sort
     * @param low  index of the first element in the range
     * @param high index of the last element in the range
     */
    public static void doublePivotQuickSort(int[] arr, int low, int high) {
        // Base case: one element arrays are already sorted
        if (low >= high) {
            return;
        }

        // Ensure the first pivot is not larger than the second
        if (arr[low] > arr[high]) {
            int tmp = arr[low];
            arr[low] = arr[high];
            arr[high] = tmp;
        }

        int pivot1 = arr[low];   // left pivot value
        int pivot2 = arr[high];  // right pivot value

        // Pointers delimiting the current partitions
        int lt = low + 1;        // items less than pivot1
        int gt = high - 1;       // items greater than pivot2
        int i = lt;              // index of the element being examined

        // Scan the array once, moving elements into one of three regions
        while (i <= gt) {
            if (arr[i] < pivot1) {             // belongs to left partition
                int tmp = arr[i];
                arr[i] = arr[lt];
                arr[lt] = tmp;
                lt++;
            } else if (arr[i] > pivot2) {      // belongs to right partition
                // move gt until a value <= pivot2 is found
                while (arr[gt] > pivot2 && i < gt) {
                    gt--;
                }
                int tmp = arr[i];
                arr[i] = arr[gt];
                arr[gt] = tmp;
                gt--;
                // after swapping we must check if the new value belongs on the left
                if (arr[i] < pivot1) {
                    tmp = arr[i];
                    arr[i] = arr[lt];
                    arr[lt] = tmp;
                    lt++;
                }
            }
            i++;
        }

        // Place the pivots in their final positions
        lt--;
        gt++;
        int tmp = arr[low];
        arr[low] = arr[lt];
        arr[lt] = tmp;
        tmp = arr[high];
        arr[high] = arr[gt];
        arr[gt] = tmp;
        // Recursively sort the three resulting partitions
        doublePivotQuickSort(arr, low, lt - 1);
        doublePivotQuickSort(arr, lt + 1, gt - 1);
        doublePivotQuickSort(arr, gt + 1, high);
    }

    public static void main(String[] args) {
        int[] data = {40, 70, 20, 90, 30, 80, 20};
        doublePivotQuickSort(data, 0, data.length - 1);
        for (int n : data) {
            System.out.print(n + " ");
        }
        System.out.println();
    }
}
