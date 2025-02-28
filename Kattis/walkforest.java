// https://open.kattis.com/problems/walkforest

import java.util.*;

public class walkforest {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        String out = "";
        Graph G;
        int n = scanner.nextInt(); // Amount of vertices
        while (n != 0) {
            int m = scanner.nextInt(); // Amount of edges
            // Construct graph:
            G = new Graph(n);
            int node1, node2, weight;
            for (int i = 0; i < m; i++) {
                node1 = scanner.nextInt();
                node2 = scanner.nextInt();
                weight = scanner.nextInt();
                G.insert(node1, node2, weight);
            }
            // Find shortest path from "home" to other crossroads:
            HashMap<Integer, Integer> dist = dijkstra(G, 1);
            // Count paths to home from work:
            int result = findPaths(G, 2, 1, dist);
            out += result + "\n";
            n = scanner.nextInt(); // Amount of vertices in next case
        }
        scanner.close();
        // Output:
        System.out.print(out);
    }

    // Counts the amount of paths from start to goal where the way to goal is from child node than parent node.
    public static int findPaths(Graph G, int start, int goal, HashMap<Integer, Integer> dist) {
        HashMap<Integer, Integer> counter = new HashMap<>();
        for (int v : G.V) {
            counter.put(v, 0);
        }
        HashSet<Integer> visited = new HashSet<>();
        Queue<Integer> queue = new LinkedList<>();
        queue.offer(start);
        visited.add(start);
        counter.put(start, 1);
        while (queue.size() != 0) {
            int v = queue.poll();
            for (int u : G.E.get(v)) {
                if (dist.get(u) >= dist.get(v))
                    continue; // Path to goal is not shortert from u than v!
                if (!visited.contains(u)) {
                    visited.add(u);
                    queue.offer(u);
                }
                counter.put(u, counter.get(v) + counter.get(u));
            }
        }
        return counter.get(goal);
    }

    // Finds shortest paths from start vertex to every other:
    public static HashMap<Integer, Integer> dijkstra(Graph G, int start) {
        HashMap<Integer, Integer> dist = new HashMap<>();
        for (int v : G.V) {
            dist.put(v, Integer.MAX_VALUE);
        }
        PriorityQueue<int[]> queue = new PriorityQueue<>(Comparator.comparingInt(a -> a[0]));
        queue.offer(new int[]{0, start});
        dist.put(start, 0);
        while (queue.size() != 0) {
            int[] poll = queue.poll();
            int v = poll[1];
            if (poll[0] > dist.get(v)) continue;
            for (int u : G.E.get(v)) {
                int fromU = dist.get(v) + G.getWeight(v, u);
                if (fromU < dist.get(u)) {
                    dist.put(u, fromU);
                    queue.offer(new int[]{fromU, u});
                }
            }
        }
        return dist;
    }

}

class Graph {
    HashSet<Integer> V = new HashSet<>();
    HashMap<Integer, HashSet<Integer>> E = new HashMap<>();
    HashMap<String, Integer> W = new HashMap<>();


    public Graph(int amountVertices) {
        initilize(amountVertices);
    }

    // Initilizes all vertices and neighbour lists from 1 to n.
    public void initilize(int n) {
        for (int i = 1; i <= n; i++) {
            V.add(i);
            E.put(i, new HashSet<>());
        }
    }

    public void insert(int node1, int node2, int weight) {
        E.get(node1).add(node2);
        E.get(node2).add(node1);
        // Add weight of edge:
        if (node1 < node2)
            W.put(node1 + "," + node2, weight);
        else
            W.put(node2 + "," + node1, weight);
    }

    public int getWeight(int node1, int node2) {
        if (node1 < node2)
            return W.get(node1 + "," + node2);
        return W.get(node2 + "," + node1);
    }

    // For debugging only:
    @Override
    public String toString() {
        String str = "";
        for (int v : V) {
            str += v + ": {";
            str += E.get(v).toString();
            str += "}\n";
        }
        return str;
    }
}