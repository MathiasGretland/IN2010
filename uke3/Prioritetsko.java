/*  Abstrakt datatype
    Bryr ikke om implementasjon
    Bryr oss kun om funksjonalitet!
*/

package uke3;

interface Prioritetsko {
    public void insert(int x); // putt på køen

    public int remove(); // fjern minste element
}

/*
 * Heap - Type: min vs max Min: - minste element ligger i rota - hver node er
 * større enn foreldre-noden
 * 
 * - komplett - peker til siste node
 * 
 */