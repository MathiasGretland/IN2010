package uke1;

public class Tre {
    Tre forelder = null;

    public void setForelder(Tre t){
        this.forelder = t;
    }

    public static int depth(Tre t){
        if (t.forelder == null){
            return -1;
        }
        return 1 + depth(t.forelder);
    }


    public static void main(String[] args) {
        Tre s = new Tre();
        Tre k = new Tre();
        Tre m = new Tre();
        Tre v = new Tre();
        s.setForelder(k);
        k.setForelder(m);
        m.setForelder(v);


        System.out.println(depth(v));
        System.out.println(depth(m));
        System.out.println(depth(k));
        System.out.println(depth(s));


    }
}
