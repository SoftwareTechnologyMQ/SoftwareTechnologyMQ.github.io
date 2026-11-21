class Rectangle {
	public double width, height;	
	
	public Rectangle(double w, double h) {
		width = w;
		height = h;
	}
	
	public String toString() {
		return width + " by " + height;
	}
}

public class ArrayOfObjects {
    public static void main(String[] args) {
        Rectangle[] blocks = new Rectangle[5];
        for(int i=0; i < blocks.length; i++) {
            System.out.println(blocks[i]);
        }

        System.out.println();
        
        for(int i=0; i < blocks.length; i++) {
            blocks[i] = new Rectangle(i+1,i*2);
        }

        System.out.println();

        for(int i=0; i < blocks.length; i++) {
            System.out.println(blocks[i]);
        }
        
        System.out.println();

        blocks[0].width = 5;

        for(int i=0; i < blocks.length; i++) {
            System.out.println(blocks[i]);
        }

        System.out.println();
        
        String str = blocks[1].toString();

        System.out.println("Second item: "+str);
    }
}