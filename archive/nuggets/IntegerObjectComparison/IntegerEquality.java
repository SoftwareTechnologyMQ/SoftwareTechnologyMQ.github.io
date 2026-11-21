package misc;

public class IntegerEquality {

	public static void main(String[] args) {
		Integer a, b;
		int[] values = {-250, -129, -128, -127, 126, 127, 128, 250};
		for(int item: values) {
			a = item;
			b = item;
			if(a == b) {
				System.out.println(a+","+b+" are SAME using ==");
			}
			else {
				System.out.println(a+","+b+" are DIFFERENT using ==");
			}	
		}
		System.out.println();

		for(int item: values) {
			a = item;
			b = item;
			if(a.equals(b)) {
				System.out.println(a+","+b+" are SAME using .equals");
			}
			else {
				System.out.println(a+","+b+" are DIFFERENT using .equals");
			}	
		}
	}

}
