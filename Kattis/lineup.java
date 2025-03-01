

import java.util.*;

public class lineup {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int n = scanner.nextInt();
        scanner.nextLine();
        ArrayList<String> liste = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            liste.add(scanner.nextLine().trim());
        }
        Boolean isInc = true;
        Boolean isDec = true;
        for (int i = 0; i < n - 1; i++) {
            if (liste.get(i).compareTo(liste.get(i + 1)) >= 0) {
                isInc = false; // List is not increasing
            }
            if (liste.get(i).compareTo(liste.get(i + 1)) <= 0) {
                isDec = false; // List is not decreasing
            }
        }

        if (isDec) {
            System.out.println("DECREASING");
        }
        else if (isInc) {
            System.out.println("INCREASING");
        }
        else {
            System.out.println("NEITHER");
        }

    }
    
}
