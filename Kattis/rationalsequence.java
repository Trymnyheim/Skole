// https://open.kattis.com/problems/rationalsequence

package Kattis;

import java.util.HashMap;
import java.util.Scanner;

public class rationalsequence {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int P = scanner.nextInt(); // Amount of fractions
        HashMap<Integer, String> results = new HashMap<>();
        for (int i = 0; i < P; i++) {
            int K = scanner.nextInt(); // Value not needed
            String frac = scanner.next();
            String[] parts = frac.split("/");
            int num = Integer.parseInt(parts[0]);
            int den = Integer.parseInt(parts[1]);
            results.put(K, findIncremented(num, den)); // Find index and add to results
        }
        scanner.close();
        // Give output:
        for (int key : results.keySet()) {
            System.out.println(key + " " + results.get(key));
        }
    }

    public static String findIncremented(int num, int den) {
        if (den == 1) {
            return 1 + "/" + (num + 1);
        }
        if (num < den) {
            return den + "/" + (den - num);
        }
        int steps = num/den;
        num = num - steps*den;
        int q_new = den - num;
        num = den;
        den = q_new + (num*steps);
        return num + "/" + den;     
    }
}
