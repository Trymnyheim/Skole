// https://open.kattis.com/problems/shortestpath1

// Wrong answer...

package Kattis;
import java.util.*;

public class shortestpath1 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        StringBuilder output = new StringBuilder();
        boolean first = true;
        
        while (true) {
            int n = scanner.nextInt(); // Number of nodes
            int m = scanner.nextInt(); // Number of edges
            int q = scanner.nextInt(); // Number of queries
            int s = scanner.nextInt(); // Start node

            // If all values are 0, break the loop
            if (n == 0 && m == 0 && q == 0 && s == 0) break;
            
            // Add a blank line between test cases
            if (!first) output.append("\n");
            first = false;

            // Create the graph
            Graph graph = new Graph(n);

            // Read edges
            for (int i = 0; i < m; i++) {
                int v = scanner.nextInt();
                int u = scanner.nextInt();
                int w = scanner.nextInt();
                graph.addEdge(v, u, w);
            }

            // Compute shortest paths from node `s`
            int[] dist = shortestPath(graph, s);

            // Process each query
            for (int i = 0; i < q; i++) {
                int target = scanner.nextInt();
                if (dist[target] == Integer.MAX_VALUE) {
                    output.append("Impossible\n");
                } else {
                    output.append(dist[target]).append("\n");
                }
            }
        }
        scanner.close();

        // Remove last newline
        if (output.length() > 0 && output.charAt(output.length() - 1) == '\n') {
            output.setLength(output.length() - 1);
        }

        // Print the output
        System.out.print(output);
    }

    // Dijkstra's algorithm for shortest paths
    public static int[] shortestPath(Graph graph, int s) {
        int[] dist = new int[graph.getSize()];
        Arrays.fill(dist, Integer.MAX_VALUE);
        dist[s] = 0;

        PriorityQueue<int[]> queue = new PriorityQueue<>(Comparator.comparingInt(a -> a[1]));
        queue.add(new int[] { s, 0 });

        while (!queue.isEmpty()) {
            int[] next = queue.poll();
            int u = next[0];
            int distU = next[1];
            for (Map.Entry<Integer, Integer> neighbor : graph.getEdges(u).entrySet()) {
                int v = neighbor.getKey();
                int weight = neighbor.getValue();
                int newDist = distU + weight;

                if (newDist < dist[v]) {
                    dist[v] = newDist;
                    queue.offer(new int[] { v, newDist });
                }
            }
        }

        return dist;
    }
}

class Graph {
    private ArrayList<HashMap<Integer, Integer>> adjacencyList;
    private int size;

    public Graph(int size) {
        this.size = size;
        adjacencyList = new ArrayList<>();
        for (int i = 0; i < size; i++) {
            adjacencyList.add(new HashMap<>());
        }
    }

    public void addEdge(int v, int u, int w) {
        adjacencyList.get(v).put(u, w);
    }

    public HashMap<Integer, Integer> getEdges(int v) {
        return adjacencyList.get(v);
    }

    public int getSize() {
        return size;
    }
}
