// https://open.kattis.com/problems/workstations

package Kattis;
import java.util.Scanner;
import java.util.Arrays;
import java.util.Comparator;
import java.util.PriorityQueue;

public class workstations {
    public static void main(String[] args) {

        Scanner scanner = new Scanner(System.in);
        int n = scanner.nextInt(); // n researchers
        int m = scanner.nextInt(); // locks after m min
        int[][] researchers = new int[n][2];
        for (int i = 0; i < n; i++) {
            researchers[i][0] = scanner.nextInt();
            researchers[i][1] = researchers[i][0] + scanner.nextInt(); // Leaving time
        }
        scanner.close();

        Arrays.sort(researchers, Comparator.comparingInt(a -> a[0]));
        PriorityQueue<Integer> avail = new PriorityQueue<>();
        int saved = 0;

        for (int[] researcher : researchers) {
            int arrival = researcher[0];
            int leave = researcher[1];
            // Remove timed out workstations:
            while (!avail.isEmpty() && avail.peek() + m < arrival) {
                avail.poll();
            }
            // Check if a workstation can be reused:
            if (!avail.isEmpty() && avail.peek() <= arrival) {
                saved++;
                avail.poll();
            }
            avail.offer(leave);
        }
        // Output:
        System.out.println(saved);
    }
}
