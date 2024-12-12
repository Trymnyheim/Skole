// https://open.kattis.com/problems/shortestpath1

// Runtime error!

package Kattis;
import java.util.*;

public class shortestpath1 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        ArrayList<List<Integer>> output = new ArrayList<>();

        while (true) {
            int n = scanner.nextInt(); // Amount of nodes
            int m = scanner.nextInt(); // Amount of edges
            int q = scanner.nextInt(); // Amount of queries
            int s = scanner.nextInt(); // Start node

            // If all values are 0, loop is broken:
            if (n == 0 && m == 0 && q == 0 && s == 0) {
                break;
            }

            // Building graph:
            Graph graph = new Graph(n);

            // Adding edges:
            for (int i = 0; i < m; i++) {
                int v = scanner.nextInt();
                int u = scanner.nextInt();
                int w = scanner.nextInt();
                graph.addEdge(v, u, w);
            }

            // Find shortest path for each query:
            List<Integer> results = new ArrayList<>();
            for (int i = 0; i < q; i++) {
                int target = scanner.nextInt();
                results.add(shortestPath(graph, s, target));
            }
            output.add(results);
        }
        scanner.close();

        // Give output:
        writeOutput(output);

    }

    // Dijsktra for finding shortest path
    public static int shortestPath(Graph graph, int s, int target) {
        if (s == target) {
            return 0;
        }
        int[] dist = new int[graph.getSize()];
        Arrays.fill(dist, Integer.MAX_VALUE);
        dist[s] = 0;

        PriorityQueue<int[]> queue = new PriorityQueue<>((a, b) -> Integer.compare(a[1], b[1]));
        queue.add(new int[]{s, 0});

        while (!queue.isEmpty()) {
            int[] next = queue.poll();
            int u = next[0];
            int dist_u = next[1];
            if (u == target) {
                break;
            }
            for (Map.Entry<Integer, Integer> neighbor : graph.getEdges(u).entrySet()) {   
                int v = neighbor.getKey();
                int c = dist_u + neighbor.getValue();
                if (c < dist[v]) {
                    dist[v] = c;
                    queue.add(new int[]{v, c});
                }
            }
        }
        if (dist[target] != Integer.MAX_VALUE) {
            return dist[target];
        }
        return -1;
    }

    public static void writeOutput(ArrayList<List<Integer>> output) {
        for (int i = 0; i < output.size(); i++) {
            List<Integer> results = output.get(i);
            for (int num : results) {
                if (num == -1) {
                    System.out.println("Impossible");
                }
                else {
                    System.out.println(num);
                }
            }
            if (i != output.size() - 1) {
                System.out.println();
            }
        }
    }
}

class Graph {
    private HashMap<Integer, HashMap<Integer, Integer>> graph;
    private int size;

    public Graph(int amountOfNodes) {
        graph = new HashMap<>();
        size = amountOfNodes;
    
        for (int i = 0; i < amountOfNodes; i++) {
            graph.put(i, new HashMap<>());
        }
    }

    public void addEdge(int v, int u, int w) {
        graph.get(v).put(u, w);
    }

    public HashMap<Integer, Integer> getEdges(int v) {
        return graph.get(v);
    }

    public int getSize() {
        return size;
    }

    public void printGraph() {
        for (Map.Entry<Integer, HashMap<Integer, Integer>> entry : graph.entrySet()) {
            System.out.print(entry.getKey() + " -> ");
            for (Map.Entry<Integer, Integer> neighbors : entry.getValue().entrySet()) {
                System.out.print("(" + neighbors.getKey() + ", " + neighbors.getValue() + ") ");
            }
            System.out.println();
        }
    }
}