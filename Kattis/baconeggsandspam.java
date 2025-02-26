// https://open.kattis.com/problems/baconeggsandspam

import java.util.*;

public class baconeggsandspam {

    public static void main(String[] args) {
        ArrayList<String> items;
        HashMap<String, ArrayList<String>> orders;
        String output = "";
        String line;
        Scanner scanner = new Scanner(System.in);
        int n = Integer.parseInt(scanner.nextLine());
        while (n != 0) {
            items = new ArrayList<>();
            orders = new HashMap<>();
            for (int i = 0; i < n; i++) {
                line = scanner.nextLine();
                String[] split = line.split("\s");
                for(int j = 1; j < split.length; j++) {
                    if (!items.contains(split[j])) 
                        items.add(split[j]); // At menu-item to items
                    if (orders.get(split[j]) == null)
                        orders.put(split[j], new ArrayList<>()); // Ensure array to store names is not null
                    if (!orders.get(split[j]).contains(split[0]));
                        orders.get(split[j]).add(split[0]); // Adds name to order's list if not there
                }
            }
            output = sortAndOutput(items, orders, output);
            n = Integer.parseInt(scanner.nextLine());
            if (n != 0)
                output += "\n";
        }
        scanner.close();
        System.out.print(output);

    }

    public static String sortAndOutput(ArrayList<String> items, HashMap<String, ArrayList<String>> orders, String output) {
        Collections.sort(items);
        ArrayList<String> names;
        for (String item : items) {
            names = orders.get(item);
            Collections.sort(names);
            output += item + " ";
            for (int i = 0; i < names.size(); i++) {
                output += names.get(i);
                if (i == names.size() - 1)
                    output += "\n";
                else
                    output += " ";
            }
        }
        return output;
    }
}