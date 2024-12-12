// https://open.kattis.com/problems/takingoutthetrash

package Kattis;
import java.util.Scanner;
import java.util.ArrayList;

public class takingoutthetrash {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int n = scanner.nextInt(); // Number of bags
        int m = scanner.nextInt(); // Max weight

        // Read input and add to list:
        ArrayList<Integer> bags = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            bags.add(scanner.nextInt());
        }
        scanner.close();
        bags.sort(null);
        
        int tripCounter = 0;
        int high = n - 1;
        int low = 0;
        while (low <= high) {
            int lowBag = bags.get(low);
            int highBag = bags.get(high);
            if (lowBag + highBag > m) {
                high--;
            }
            else {
                low++;
                high--;
            }
            tripCounter++;
        }
        System.out.println(tripCounter);
    }
}
