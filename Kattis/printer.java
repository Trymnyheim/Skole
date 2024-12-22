package Kattis;

import java.util.Scanner;

public class printer {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int target = sc.nextInt();
        sc.close();
        int printers = 1;
        int days = 0;
        while (printers < target) {
            printers *= 2;
            days++;
        }
        days++;
        System.out.println(days);
    }
}
