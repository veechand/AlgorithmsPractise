package practise;

/**
 * @author veechand
 *
 */
public class MinHeap<T extends Comparable<T>> {
	private IndexedOneArray<T> heap = new IndexedOneArray<T>();
	
	public void add (T element){
		heap.add(element);
		for(int i=heap.size()/2;i>=1;i=i/2){
			minHeapify(i);
		}
	}
	
	public T deleteMin(){
		T element = heap.get(1);
		heap.set(1, heap.get(heap.size()));
		heap.remove(heap.size());
		minHeapify(1);
		return element;
	}
	public void minHeapify(int index) {
		int minIndex=-1;
		if(heap.isRightAvbl(index)){
			minIndex = heap.get(index*2).compareTo(heap.get((index*2)+1))<0?index*2:(index*2)+1;
		} else if(heap.isLeftAvbl(index)){
			minIndex=index*2;
		}
		if(minIndex != -1){
			if(heap.get(index).compareTo(heap.get(minIndex))>0){
				swap(index, minIndex);
				minHeapify(minIndex);
			}
		}
	}

	private void swap(int index, int minIndex) {
		T parent = heap.get(index);
		heap.set(index, heap.get(minIndex));
		heap.set(minIndex,parent);
	}
	
	@Override
	public String toString(){
		return heap.toString();
	}

	public boolean empty() {
		return heap.size() <= 0;
	}

	public int size() {
		return heap.size();
	}
}
