import java.util.Arrays;

class Point {
	public int x, y;
	
	public Point(int x, int y) {
		this.x = x; //"this" distinguishes instance variable from formal paramter
		this.y = y;
	}
	
	public Point(Point p) {
		x = p.x;
		y = p.y;
	}
	
	public String toString() {
		return "("+x+","+y+")";
	}
}

class ConnectTheDots {
	public Point[] points;
	
	public ConnectTheDots(Point[] source) {
		if(source == null) {	
			points = new Point[0];
		}
		else {
			int nonNullPoints = 0;
			
			for(int i=0; i < source.length; i++) {
				if(source[i] != null) {
					nonNullPoints++;
				}
			}
			
			points = new Point[nonNullPoints];
			
			int k = 0; //destination index
			for(int i=0; i < source.length; i++) {
				if(source[i] != null) {
					points[k] = source[i];
					k++;
				}
			}
		}
	}
}

public class ArtGallery {
	public static void main(String[] args) {
		Point a = new Point(30, 10);
		Point b = new Point(50, 30);
		Point c = null;
		Point d = new Point(30, 50);
		Point e = new Point(10, 30);
		Point[] src = {a, b, c, d, e};
		ConnectTheDots canvas = new ConnectTheDots(src);
		System.out.println(Arrays.toString(canvas.points));
	}
}
