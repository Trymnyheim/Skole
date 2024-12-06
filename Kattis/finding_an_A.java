// https://open.kattis.com/problems/findingana

package Kattis;
import java.util.Scanner;

public class finding_an_A {
    public static void main(String[] args){
        Scanner scanner = new Scanner(System.in);
        String word = scanner.nextLine();
        scanner.close();
        String output = "";
        Boolean include = false;
        for (int i = 0; i < word.length(); i++) {
            if (word.charAt(i) == 'a') {
                include = true;
            }
            if (include) {
                output += word.charAt(i);
            }
        }
        System.out.println(output);
    }
}
