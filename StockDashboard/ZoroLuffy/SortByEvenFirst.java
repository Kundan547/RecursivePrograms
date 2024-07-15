package StockDashboard.ZoroLuffy;
public class SortByEvenFirst {

    public static void sortByEvenFirst(int[] arr) {
        int nextEven = 0;
        int nextOdd = arr.length - 1;

        while (nextEven < nextOdd) {
            if (arr[nextEven] % 2 == 0) {
                nextEven++;
            } else if (arr[nextOdd] % 2 != 0) {
                nextOdd--;
            } else {
                int temp = arr[nextEven];
                arr[nextEven] = arr[nextOdd];
                arr[nextOdd] = temp;
                nextEven++;
                nextOdd--;
            }
        }
    }

    public static void main(String[] args) {
        int[] arr = {1, 4, 3, 2, 5};
        sortByEvenFirst(arr);
        System.out.println(java.util.Arrays.toString(arr));
    }
}