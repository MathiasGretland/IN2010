package kattis;

import java.util.Scanner;

public class Pet {
    public static void main(String[] args) {
        int vinner = 0;
        int vinnerTall = 0;
        Scanner sc = new Scanner(System.in);
        while (sc.hasNextInt()) {
            int king = sc.nextInt();
            int queen = sc.nextInt();
            int rooks = sc.nextInt();
            int bishops = sc.nextInt();
            int samling = king + queen + rooks + bishops;
            if (samling > vinner){
                vinner = samling;
                vinnerTall++;
            }
            if (sc.equals(5)){
                System.exit(0);
            }

        }
        System.out.println(vinner);
        System.out.println(vinnerTall);
    }
}