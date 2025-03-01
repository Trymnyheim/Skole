import java.util.Scanner;

public class toilet {
    
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        String str = scanner.nextLine();
        System.out.println(upordown(str, 'U'));
        System.out.println(upordown(str, 'D'));
        System.out.println(asyoulike(str));
        

    }

    public static int upordown(String str, char custom) {
        int total = 0;
        char current = str.charAt(0);
        for (int i = 1; i < str.length(); i++) {
            if (str.charAt(i) != current) {
                total++;
                current = str.charAt(i);
            }
            if (current != custom) {
                current = custom;
                total++;
            }
        }
        return total;
    }

    public static int asyoulike(String str) {
        int total = 0;
        char current = str.charAt(0);
        for (int i = 1; i < str.length(); i++) {
            if (current != str.charAt(i)) {
                total++;
                current = str.charAt(i);
            }
        }
        return total;
    }
}
