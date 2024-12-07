// https://open.kattis.com/problems/mirror

package Kattis;
import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class mirror {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int T = scanner.nextInt();
        scanner.nextLine();
        List<String[]> testCases = new ArrayList<>();
        for (int i = 0; i < T; i++) {
            int R = scanner.nextInt();
            int C = scanner.nextInt();
            scanner.nextLine();
            String[] test = new String[R];
            for (int j = R - 1; j >= 0; j--) {
                String line = scanner.nextLine();
                String reverse = "";
                for (int k = C - 1; k >= 0; k--) {
                    reverse = reverse + line.charAt(k);
                }
                test[j] = reverse;
            }
            testCases.add(test);
        }
        scanner.close();

        // Giving output:
        int i = 1;
        for (String[] array : testCases) {
            System.out.println("Test " + i);
            for (String element : array) {
                System.out.println(element);
            }
            i++;
        }
    }
}
