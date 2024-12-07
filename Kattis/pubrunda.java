// https://open.kattis.com/problems/pubrunda

package Kattis;
import java.util.Scanner;

public class pubrunda {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int N = scanner.nextInt();
        String maxName = "";
        int maxLength = 0;
        for (int i = 0; i < N; i++) {
            String barName = scanner.next();
            int length = (scanner.nextInt() + 1) * scanner.nextInt();
            if (length > maxLength) {
                maxName = barName;
                maxLength = length;
            }
        }
        System.out.print(maxName + " ");
        System.out.println(maxLength);
    }
}
