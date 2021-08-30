package uke1;

public class Sokefunksjon {

    public boolean finnElement(String [] a, String x){
        for (String y : a){
            if (y.equals(x)){
                return true;
            }
        }
        return false;
    }


    public static void main(String[] args) {
        Sokefunksjon swag = new Sokefunksjon();
        String [] array = {"Swag", "kekw", "lol"};
        String x = "Swag";
        String xd = "nei";
        System.out.println(swag.finnElement(array, x));
        System.out.println(swag.finnElement(array, xd));
    }
}
