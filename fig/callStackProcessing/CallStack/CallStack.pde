void setup() {
 	int ax = 1, ay = 3;
	int bx = 6, by = 5;
	float d = distance(ax, ay, bx, by);
	println("Distance: "+d);
}

float distance(int x1, int y1, int x2, int y2) {
	int s1 = square(x2-x1);
	int s2 = square(y2-y1);
	int sumSquares = s1 + s2;
	float result = (float)Math.sqrt(sumSquares);
  return result;
}

int square(int num) {
	int answer = num * num;
	return answer;
}
