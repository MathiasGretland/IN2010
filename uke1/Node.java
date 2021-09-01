package uke1;

public class Node{
    int data;
    Node left;
    Node right;
    Node (int data){
        this.data = data;
    }
    public static Node insert(Node n, int element){
        if (n.data == 0){
            n = new Node(element);
        } else if (element < n.data){
            insert(n.left, element);
        } else if (element > n.data){
            insert(n.right, element);
        }
        return n;

    }

    public static void main(String[] args) {
        Node start = new Node(0);
        int i = 2;
        insert(start, i);
    }
}
