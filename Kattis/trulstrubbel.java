import java.util.*;

public class trulstrubbel {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        String game = scanner.nextLine();
        int H = 0;
        int T = 0;
        for (int i = 0; i < game.length(); i++) {
            char winner = game.charAt(i);
            if (winner == 'H') {
                H++;
            } else {
                T++;
            }
            if (H >= 11 || T >= 11) {
                if (Math.abs(H - T) >= 2) {
                    T = 0; H = 0;
                }
            }
        }
        System.out.println(T + "-" + H);
    }
}