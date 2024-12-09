// https://open.kattis.com/problems/eatingout

package Kattis;
import java.util.Scanner;

public class eatingout {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int m = scanner.nextInt();
        int a = scanner.nextInt();
        int b = scanner.nextInt();
        int c = scanner.nextInt();
        scanner.close();
        if (a + b + c - 2* m <= 0) {
            System.out.println("possible");
        }
        else {
            System.out.println("impossible");
        }
    }
}
