// https://open.kattis.com/problems/rationalsequence2

package Kattis;
import java.util.HashMap;
import java.util.Scanner;

public class rationalsequence2 {
    
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int P = scanner.nextInt(); // Amount of fractions
        HashMap<Integer, Long> results = new HashMap<>();
        for (int i = 0; i < P; i++) {
            int K = scanner.nextInt(); // Value not needed
            String frac = scanner.next();
            String[] parts = frac.split("/");
            long num = Integer.parseInt(parts[0]);
            long den = Integer.parseInt(parts[1]);
            results.put(K, solve(num, den)); // Find index and add to results
        }
        scanner.close();
        // Give output:
        for (int key : results.keySet()) {
            System.out.println(key + " " + results.get(key));
        }
    }

    private static long solve(long num, long den) {
        String path = "";
        while (!(num == 1 && den == 1)) {
            if (num > den) {
                num -= den;
                path += ("R");
            }
            else {
                den -= num;
                path += ("L");
            }
        }
        // Retrace path:
        long pos = 0;
        for (int i = path.length() - 1; i >= 0; i--) {
            if (path.charAt(i) == 'L')
                pos = pos * 2 + 1;
            else
                pos = pos * 2 + 2;
        }
        return pos + 1;
    }
}

