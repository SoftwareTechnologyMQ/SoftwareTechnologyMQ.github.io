import java.util.ArrayList;
import java.util.List;

public class TreeSort {
    private static class Node {
        int value;
        Node left;
        Node right;
        Node(int v) {
            value = v;
        }
    }

    private static void insert(Node root, int value) {
        if (value <= root.value) {
            if (root.left == null) {
                root.left = new Node(value);
            } else {
                insert(root.left, value);
            }
        } else {
            if (root.right == null) {
                root.right = new Node(value);
            } else {
                insert(root.right, value);
            }
        }
    }

    private static void inorder(Node node, List<Integer> out) {
        if (node != null) {
            inorder(node.left, out);
            out.add(node.value);
            inorder(node.right, out);
        }
    }

    public static void treeSort(int[] arr) {
        if (arr.length == 0) {
            return;
        }
        Node root = new Node(arr[0]);
        for (int i = 1; i < arr.length; i++) {
            insert(root, arr[i]);
        }
        List<Integer> result = new ArrayList<>();
        inorder(root, result);
        for (int i = 0; i < arr.length; i++) {
            arr[i] = result.get(i);
        }
    }

    public static void main(String[] args) {
        int[] data = {40, 70, 20, 90, 30, 80, 20};
        treeSort(data);
        for (int n : data) {
            System.out.print(n + " ");
        }
        System.out.println();
    }
}
