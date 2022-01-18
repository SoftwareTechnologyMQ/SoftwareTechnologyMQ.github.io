public class RNode {
	private Rectangle data;
	private RNode next;

	public Rectangle getData() {
		return data;
	}

	public RNode getNext() {
		return next;
	}

	public void setData(Rectangle d) {
		data = d;
	}

	public void setNext(RNode n) {
		next = n;
	}

	public RNode(Rectangle d, RNode n) {
		setData(d);
		setNext(n);
	}
}
