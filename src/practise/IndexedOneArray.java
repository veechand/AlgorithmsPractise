/**
 * 
 */
package practise;

import java.util.ArrayList;
import java.util.List;

/**
 * @author veechand
 * 
 * This does a subset of functionalities done by List, but all the 
 * methods in this are indexed by one  
 */
public class IndexedOneArray<T extends Comparable<T>> {

	private List<T> dataHolder = new ArrayList<T>();
	
	/**
	 * @param args
	 */
	public static void main(String[] args) {
		IndexedOneArray<Integer> dataHolder = new IndexedOneArray<Integer>();
		dataHolder.add(10);
		dataHolder.add(20);
		System.out.println(dataHolder);
		System.out.println(dataHolder.get(1));
		System.out.println(dataHolder.size());
		System.out.println(dataHolder.isLeftAvbl(1));
		System.out.println(dataHolder.isRightAvbl(1));
		dataHolder.set(2, 30);
		System.out.println(dataHolder);
		System.out.println(dataHolder.size());
		dataHolder.remove(2);
		System.out.println(dataHolder);
		System.out.println(dataHolder.size());
		System.out.println(dataHolder.isLeftAvbl(1));
		System.out.println(dataHolder.isRightAvbl(1));
	}
	
	public void add(T value){
		dataHolder.add(value);
	}
	public void set(int index,T value){
		dataHolder.set(index-1, value);
	}
	
	public T get(int index){
		return dataHolder.get(index-1);
	}
	
	public T remove(int index){
		return dataHolder.remove(index-1);
	}
	
	public int size(){
		return dataHolder.size();
	}
	
	public boolean isLeftAvbl(int index){
		return size() >= index*2;
	}
	
	public boolean isRightAvbl(int index){
		return size() >= (index*2) +1;
	}

	@Override
	public String toString(){
		return dataHolder.toString();
	}
}
