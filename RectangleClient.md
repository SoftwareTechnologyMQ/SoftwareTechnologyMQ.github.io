```java
import java.util.LinkedList;
import java.util.Random;

public class RectangleClient {

	public static LinkedList<Rectangle> generateList(int n, int minSide, int maxSide) {
		new LinkedList<Rectangle>();
		LinkedList<Rectangle> result = new LinkedList<Rectangle>();
		Random rand = new Random();
		for(int i=0; i < n; i++) {
			int w = rand.nextInt(8) + 1; //to get random integer between 1 an 8
			int h = rand.nextInt(8) + 1; //to get another random integer between 1 an 8
			Rectangle r = new Rectangle(w, h);
			result.add(r);
		}
		return result;
	}

	public static void displayRectanglesAreaMoreThan(LinkedList<Rectangle> data, int threshold) {
		for(int i=0; i < data.size(); i++) {
			if(data.get(i).area() >= threshold) {
				System.out.println(data.get(i));
			}
		}
	}

	public static int firstIndexBiggerThanNext(LinkedList<Rectangle> data) {
		for(int i=0; i < data.size() - 1; i++) { //for all but last
			if(data.get(i).area() > data.get(i+1).area()) { //found it
				return i;
			}
		}
		return -1; //no such rectangle exists
	}

	public static int getBiggestIndex(LinkedList<Rectangle> data) {
		int maxIndex = 0; //assume first rectangle is the biggest
		for(int i=1; i < data.size(); i++) {
			int currentArea = data.get(i).area();
			int biggestArea = data.get(maxIndex).area();
			if(currentArea > biggestArea) { //found bigger rectangle
				maxIndex = i; //update index of biggest rectangle
			}
		}
		return maxIndex;
	}

	public static LinkedList<Rectangle> getSquares(LinkedList<Rectangle> data) {
		LinkedList<Rectangle> result = new LinkedList<Rectangle>();
		for(int i=0; i < data.size(); i++) {
			if(data.get(i).isSquare()) {
				result.add(data.get(i));
			}
		}
		return result;
	}

	public static void main(String[] args) {
		LinkedList<Rectangle> rectangles = generateList(20, 1, 8);

		displayRectanglesAreaMoreThan(rectangles, 10);

		int idx = firstIndexBiggerThanNext(rectangles);
		if(idx >= 0) {
			System.out.println("First rectangle bigger than the next rectangle: "+idx);
		}
		else {
			System.out.println("No rectangle is bigger than the next rectangle");
		}

		int indexBiggest = getBiggestIndex(rectangles);
		System.out.println("Area of biggest rectangle: "+rectangles.get(indexBiggest).area());

		LinkedList<Rectangle> squareList = getSquares(rectangles);
		System.out.println("Squares: "+squareList);
	}
}
```
