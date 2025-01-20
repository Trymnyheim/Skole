package Kattis;

import java.util.Scanner;

public class ABC {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int[] nums = new int[3];
        for (int i = 0; i < nums.length; i++) {
            nums[i] = scanner.nextInt();
        }
        selectionSort(nums);
        String order = scanner.next();
        scanner.close();
        for (int i = 0; i < 3; i++) {
            if (order.charAt(i) == 'A')
                System.out.print(nums[0]);
            if (order.charAt(i) == 'B')
                System.out.print(nums[1]);
            if (order.charAt(i) == 'C')
                System.out.print(nums[2]);
            if (i == 2)
                System.out.println();
            else
                System.out.print(" ");
        }
    }

    public static void selectionSort(int[] nums) {
        for (int i = 0; i < nums.length - 1; i++) {
            int min = i;
            for (int j = i + 1; j < nums.length; j++) {
                if (nums[j] < nums[min])
                    min = j;
            }
            if (min != i) {
                int minVal = nums[min];
                nums[min] = nums[i];
                nums[i] = minVal;
            }
        }
    }
}