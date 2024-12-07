// https://open.kattis.com/problems/whichisgreater
package Kattis;
import java.util.Scanner;

class whichisgreater{
    public static void main(String[] args){
        Scanner scanner = new Scanner(System.in);
        int number1 = scanner.nextInt();
        int number2 = scanner.nextInt();
        scanner.close();
        int output = 0;
        if (number1 > number2){
            output = 1;
        }
        System.out.println(output);
    }

}