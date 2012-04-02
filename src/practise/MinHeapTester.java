/**
 * 
 */
package practise;

/**
 * @author veechand
 *
 */
public class MinHeapTester {

	/**
	 * @param args
	 */
	public static void main(String[] args) {
		MinHeap<Integer> heap = new MinHeap<Integer>();
		heap.add(10);
		heap.add(12);
		heap.add(9);
		heap.add(15);
		System.out.println(heap);
		System.out.println(heap.deleteMin());
		System.out.println(heap);

	}

}

