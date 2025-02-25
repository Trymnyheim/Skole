// https://open.kattis.com/problems/aprizenoonecanwin

import java.util.*;

public class Aprizenoonecanwin {

    public static void main(String[] args) {
        
        // Read input:
        Scanner scanner = new Scanner(System.in);
        int n = scanner.nextInt();
        int x = scanner.nextInt();
        ArrayList<Integer> prices = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            prices.add(scanner.nextInt());
        }
        scanner.close();

        // Solve and give output:
        int result = solve(n, x, prices);
        System.out.println(result);
    }

    private static int solve(int n, int x, ArrayList<Integer> prices) {
        Collections.sort(prices);
        int i = n - 1;
        int counter = 0;
        int total;
        while (i >= 1) {
            total = prices.get(i) + prices.get(i - 1);
            if (x < total) counter++;
            else i = 0;
            i--;
        }
        return n - counter;
    }
}
