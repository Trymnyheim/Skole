// https://open.kattis.com/problems/blackfriday

package Kattis;
import java.util.Scanner;
import java.util.HashMap;

public class blackfriday {
    public static void main(String[] args){
        Scanner scanner = new Scanner(System.in);
        int N = scanner.nextInt();
        HashMap<Integer, Integer> map = new HashMap<Integer, Integer>();
        for (int i = 1; i < N + 1; i++) {
            int num = scanner.nextInt();
            if (map.containsKey(num)) {
                map.put(num, 0);
            }
            else {
                map.put(num, i);
            }
        }
        scanner.close();
        for (int i = 6; i >= 0; i--) {
            if (map.containsKey(i)){
                int result = map.get(i);
                if (result != 0) {
                    System.out.println(result);
                    break;
                }
            }
            if (i == 0) {
                System.out.println("none");
            }
        }
    }
}