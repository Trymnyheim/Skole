// https://open.kattis.com/problems/cookingwater

package Kattis;
import java.util.Scanner;

public class cookingwater {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int N = scanner.nextInt();
        int min = -1; // min value of a is 0
        int max = 1001; // max value of b is 1000
        for (int i = 0; i < N; i ++) {
            int a = scanner.nextInt();
            int b = scanner.nextInt();
            min = Math.max(min, a);
            max = Math.min(max, b);
        }
        scanner.close();

        // Give output:
        if (min <= max) {
            System.out.println("gunilla has a point");
        }
        else {
            System.out.println("edward is right");  
        }
    }
}
