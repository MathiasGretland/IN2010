package uke5;

public class Schjetne{
    public static void main(String[] args){

        double sum = 0;
        int value = 100000;
        for (double i = 1; i <= value; i += 2){
            sum += 1 / i;
            i += 2;
            sum -= 1 / i;
        }
        double pi = 4 * sum;

        System.out.println(pi);
    }
}