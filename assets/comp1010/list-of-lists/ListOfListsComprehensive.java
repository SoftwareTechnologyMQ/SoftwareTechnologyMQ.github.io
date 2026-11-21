import java.util.*;

public class ListOfListsComprehensive {
    public static void main(String[] args) {
        ArrayList<Integer> a = new ArrayList<Integer>(Arrays.asList(10, 70, 20, 90));
        ArrayList<Integer> b = new ArrayList<Integer>(Arrays.asList(50, 30));
        ArrayList<Integer> c = null;
        ArrayList<Integer> d = new ArrayList<Integer>(Arrays.asList(60, null, 30));
        ArrayList<ArrayList<Integer>> varying = 
                        new ArrayList<ArrayList<Integer>>(Arrays.asList(a, b, c, d));

        if(varying!=null) {
            int maxItems = 0;
            for(int i=0; i < varying.size(); i++) {
                if(varying.get(i)!=null) {
                    maxItems = Math.max(maxItems, varying.get(i).size());
                }
            }
            
            for(int i=0; i < maxItems; i++) {
                for(int k=0; k < varying.size(); k++) {
                    if(varying.get(k)!=null) {
                        if(varying.get(k).size() > i) {
                            System.out.println(varying.get(k).get(i));
                        }
                        else {
                            System.out.println("out of bounds");
                        }
                    }
                    else {
                        System.out.println("list is null");
                    }
                }
                System.out.println("----");
            }
        }
    }
}