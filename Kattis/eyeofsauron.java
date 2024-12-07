// https://open.kattis.com/problems/eyeofsauron

package Kattis;
import java.util.Scanner;

public class eyeofsauron {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        String input = scanner.next();
        scanner.close();

        // Give output based on balance:
        if (isEyeBalanced(input)) {
            System.out.println("correct");
        }
        else {
            System.out.println("fix");
        }
    }

    // Checks if balance is equal in eye:
    public static Boolean isEyeBalanced(String eye) {
        int[] lengths = {0, 0};
        int counter = 0;
        for (int i = 0; i < eye.length(); i++) {
            if (eye.charAt(i) == '|') {
                counter++;
            }
            else if (counter != 0) {
                lengths[0] = counter;
                counter = 0;
            }
        }
        lengths[1] = counter;
        if (lengths[0] == lengths[1]) {
            return true;
        }
        return false;
    }
}