// https://open.kattis.com/problems/borders

// Assignment slightly misunderstood.
// My code counts the regions instead of counting the amount of borders needed
// to surround each region.

package Kattis;
import java.util.ArrayList;
import java.util.HashSet;
import java.util.Scanner;

public class borders {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int m = sc.nextInt();
        char[][] image = new char[n][m];
        for (int i = 0; i < n; i++) {
            String next = sc.next();
            for (int j = 0; j < m; j++) {
                image[i][j] = next.charAt(j);
            }
        }
        sc.close();

        HashSet<String> visited = new HashSet<>();
        int counter = 0;
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                String key = i + "," + j;
                if (!visited.contains(key)) {
                    visit(i, j, visited, image, n, m);
                    counter++;
                }
            }
        }
        System.out.println(counter);
    }

    public static void visit(int i, int j, HashSet<String> visited, char[][] image, int n, int m) {
        visited.add(i + "," + j);
        ArrayList<int[]> neighbours = getNeighbours(i, j, visited,n, m);
        if (!neighbours.isEmpty()) {
            for (int[] neigh : neighbours ) {
                if (image[neigh[0]][neigh[1]] == image[i][j]) {
                    if (!visited.contains(neigh[0] + "," + neigh[1]))
                        visit(neigh[0], neigh[1], visited, image, n, m);
                }
            }
        }
    }

    public static ArrayList<int[]> getNeighbours(int i, int j, HashSet<String> visited, int n, int m) {
        ArrayList<int[]> neighbours = new ArrayList<>();
        ArrayList<int[]> suggestions = new ArrayList<>();
        int[] up = {i - 1, j};
        suggestions.add(up);
        int[] down = {i + 1, j};
        suggestions.add(down);
        int[] left = {i, j - 1};
        suggestions.add(left);
        int[] right = {i, j + 1};
        suggestions.add(right);
        for (int[] neigh : suggestions) {
            if (neigh[0] < 0 || neigh[0] >= n || neigh[1] < 0 || neigh[1] >= m)
                continue;
            if (!visited.contains(neigh[0] + "," + neigh[1]))
                neighbours.add(neigh);
        }
        return neighbours;
    }
}
