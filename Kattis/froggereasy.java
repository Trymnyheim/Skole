import java.util.*;

public class froggereasy {
    
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int n = scanner.nextInt();
        int s = scanner.nextInt();
        int m = scanner.nextInt();
        int[] board = new int[n];
        for (int i = 0; i < n; i++) {
            board[i] = scanner.nextInt();
        }
        int res = makeMove(board, s - 1, m, 0, new HashSet<>());
        System.out.println(res);
    }

    public static int makeMove(int[] board, int frogPos, int magic, int counter, HashSet<Integer> visited) {
        if (!visited.contains(frogPos)) {
            visited.add(frogPos);
        }
        else {
            System.out.println("cycle");
            return counter;
        }
        if (board[frogPos] == magic) {
            System.out.println("magic");
            return counter;
        }
        frogPos += board[frogPos];
        counter++;
        if (frogPos < 0) {
            System.out.println("left");
            return counter;
        }
        if (frogPos >= board.length) {
            System.out.println("right");
            return counter;
        }
        return makeMove(board, frogPos, magic, counter, visited);
    }
}
