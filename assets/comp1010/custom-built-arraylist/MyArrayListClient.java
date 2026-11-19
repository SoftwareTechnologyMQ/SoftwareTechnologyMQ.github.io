public class MyArrayListClient {
  public static void main(String[] args) {
    MyArrayList list = new MyArrayList();
    for(int i=0; i < 6; i++) {
      list.add(2*i+1);
    }
    System.out.println("After populating with 6 items: "+list);
    list.add(2, 100);
    System.out.println("After adding 100 at index 2: "+list);
    list.add(0, -10);
    System.out.println("After adding -10 at index 0: "+list);
    list.remove(1);
    System.out.println("After removing item at index 1: "+list);
    list.remove(list.size()-1);
    System.out.println("After removing last item: "+list);
  }
}
