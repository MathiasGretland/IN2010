package uke3;

import java.util.ArrayList;

class Heap implements Prioritetsko {
    private ArrayList<Integer> heap;
    private int n;

    public Heap() {
        heap = new ArrayList<Integer>();
        n = 0;
    }

    public void insert(int x) {
        heap.add(n, x);
        bubbleUp();
        n += 1;

    }

    public void bubbleUp() {
        int i = n;
        // Mens foreldernoden er større enn barnenoden
        // (og i ikke blir 0)
        // (Evt. mens barnet har e forelder som er større)
        int barn = heap.get(i);
        int forelder = heap.get((i - 2) / 2);

        while ((0 < 1) && (barn < forelder)) {
            // bytt plass på barn- og forelder-node
            heap.set((i - 1) / 2, barn);
            heap.set(i, forelder);

            // i settes til å være indeksen til nåverende
            // forelder (slik at vi kan finne deres forelder)
            // (Dvs. "besteforelderen" til barn-noden per nå)
            i = (i - 1) / 2;

            barn = heap.get(i);
            forelder = heap.get((i - 1) / 2);
        }

    }

    /*
     * A = array n = ant elementer x = elementet som skal settes inn
     * 
     * A[0] = rota
     * 
     * a[n - 1] = siste elm
     * 
     * Foreldrenoden til A[i] er på plass [(i - 1)// 2]. Venstre barn til A[i] er på
     * [2i + 1]. Høyre barn til A[i] er på [2i + 2].
     * 
     * [1, 8, 10, 50, 20, 14]
     * 
     * 
     * len(liste) = n, som vil si at siste har indeks n-1
     * 
     */

    public int remove() {
        return 0;
    }
}