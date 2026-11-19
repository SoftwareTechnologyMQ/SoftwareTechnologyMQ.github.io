public class Point {
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
