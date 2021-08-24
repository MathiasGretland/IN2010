package kattis;

import java.util.Scanner;

public class Bijele {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        while (sc.hasNextInt()) {
            int king = sc.nextInt();
            int queen = sc.nextInt();
            int rooks = sc.nextInt();
            int bishops = sc.nextInt();
            int knights = sc.nextInt();
            int pawns = sc.nextInt();
            if (king == 1){
                king = 0;
            }else if (king == 0){
                king = 1;
            }else if (king > 1){
                king = -king+1;
            }
            if (queen == 1){
                queen = 0;
            }else if (queen == 0){
                queen = 1;
            }else if (queen > 1){
                queen = -queen+1;
            }
            if (rooks == 2){
                rooks = 0;
            }else if (rooks >= 0 && rooks < 2){
                rooks = 2 - rooks;
            }else if (rooks > 2){
                rooks = -rooks+2;
            }
            if (bishops == 2){
                bishops = 0;
            }else if (bishops >= 0 && bishops < 2){
                bishops = 2 - bishops;
            }else if (bishops > 2){
                bishops = -bishops+2;
            }
            if (knights == 2){
                knights = 0;
            }else if (knights >= 0 && knights < 2){
                knights = 2 - knights;
            }else if (knights > 2){
                knights = -knights+2;
            }
            if (pawns == 8){
                pawns = 0;
            }else if (pawns >= 0 && pawns < 8){
                pawns = 8 - pawns;
            }else if (pawns > 8){
                pawns = -pawns+8;
            }
            System.out.println(king + " " + queen + " " + rooks + " " + bishops + " " + knights + " " + pawns);
        }
    }
}
