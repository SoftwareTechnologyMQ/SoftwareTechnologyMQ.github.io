public class MyArrayList {
	private double[] data;
	private int nItems;

	public MyArrayList() {
		data = new double[5];
		nItems = 0; //no item added yet
	}

	public int size() {
		return nItems;
	}

	public boolean isFull() {
		if(nItems == data.length) {
			return true;
		}
		else {
			return false;
		}
	}

	//grow the array. if not full, don't do anything
	private void grow() { //private because we don't want clients to call it
		double[] temp = new double[data.length + 5]; //5 extra items

		for(int i=0; i < data.length; i++) { //copy all items over
			temp[i] = data[i];
		}

		data = temp; //make instance variable array refer to the bigger array
	}

	//add itemToAdd at the end of the list
	public void add(double itemToAdd) {
		if(isFull()) {
			grow();
		}
		data[nItems] = itemToAdd;
		nItems++;
	}

	// add itemToAdd at index idx and return true (return false if invalid index)
	//remember that we can add an item after the last item (eg., at index 5 if list contains 5 items)
	public boolean add(int idx, double itemToAdd) {
		if(idx < 0 || idx > nItems) {
			return false; //to indicate failure
		}

		if(isFull()) {
			grow();
		}
		for(int i=nItems - 1; i >= idx; i--) {
			data[i+1] = data[i];
		}

		data[idx] = itemToAdd;
		nItems++;

		return true; //to indicate success
	}

	//remove and return item at index idx. return null if invalid index
	public Double remove(int idx) {
		if(idx < 0 || idx >= nItems) {
			return null; //error code
		}

		double itemToRemove = data[idx];

		for(int i=idx; i < nItems - 1; i++) {
			data[i] = data[i+1];
		}
		nItems--;

		return itemToRemove; //can return double variable as Double
	}

	public String toString() {
		if(nItems == 0) {
			return "[]";
		}
		String result = "[";
		for(int i=0; i < nItems; i++) {
			result = result + data[i] + ", ";
		}
		result = result.substring(0,result.length()-2); //to remove last ", "
		result = result + "]";
		return result;
	}

	//think
	public boolean isEmpty() {
		return false; //to be completed
	}

	//return true if passed index is valid (has an item at that index), false otherwise
	public boolean isValidIndex(int idx) {
		return false; //to be completed
	}

	//think
	public boolean contains(double target) {
		return false; //to be completed
	}

	//think
	public int indexOf(double target) {
		return -1; //to be completed
	}

	//think
	public int lastIndexOf(double target) {
		return -1; //to be completed
	}

	//return true if there is one and only one instance of target, false otherwise
	public boolean containsOneAndOnlyOneOf(double target) {
		return false; //to be completed
	}

	//replace item at index idx (if it exists) by newValue and return the replaced value, return null if index is invalid
	public Double replace(int idx, double newValue) {
		return null; //to be completed
	}

	//remove all occurrences of target and return number of occurrences removed
	public int removeAll(double target) {
		return 0; //to be completed
	}

	//add target after first occurrence of pivot (if any) and return true. don't add target if pivot doesn't exist and return false.
	public boolean addAfter(double pivot, double target) {
		return false; //to be completed
	}

	//add target before first occurrence of pivot (if any) and return true. don't add target if pivot doesn't exist and return false.
	public boolean addBefore(double pivot, double target) {
		return false; //to be completed
	}

	//return MyArrayList object containing items from startIndex to endIndex (inclusive on both sides)
	public MyArrayList sublist(int startIndex, int endIndex) {
		return null; //to be completed
	}

	//resize the array to the exact same size required to hold the items there exist.
	//for example, if data.length is 10 but nItems is 7,
	//create an array of size 7, copy items over and re-reference instance variable array
	//PS I understand this is a rather useless method in real life
	public void shrinkToFit() {
			return; //to be completed
	}

	//add all items of the other to the calling object
	public void addAll(MyArrayList other) {
		return; //to be completed
	}
}
