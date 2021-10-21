
public class linkedList {
    public class Node {
        int data;
        Node prev;
        Node next;

        public Node(int data) {
            this.data = data;
            prev = null;
            next = null;
        }
    }

    Node head;
    Node tail;
    int size;

    public linkedList() {
        head = null;
        tail = null;
        size = 0;
    }

    public String toString() {
        String listString = "[";

        Node currentNode = head;
        while (currentNode != null) {
            listString += currentNode.data;
            currentNode = currentNode.next;

            if (currentNode != null) {
                listString += ", ";
            }
        }

        listString += "]";

        return listString;
    }

    public void push(int data) {
        if (size == 0) {
            Node newNode = new Node(data);
            head = newNode;
            tail = newNode;
        } else {
            Node newNode = new Node(data);
            tail.next = newNode;
            newNode.prev = tail;
            tail = newNode;
        }
        size++;
    }

    public int peek() {
        return tail.data;
    }

    public static void main(String[] args) {
        linkedList mylis = new linkedList();
        for (int i = 0; i < 100; i++) {
            mylis.push(i);
        }
        System.out.println(mylis.peek());
    }
}