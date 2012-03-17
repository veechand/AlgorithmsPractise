/**
 * 
 */
package practise;

import java.util.ArrayList;
import java.util.LinkedList;

/**
 * @author moonpearl
 *
 */
public class LinkedDisjointSetTester {

	/**
	 * @param args
	 */
	public static void main(String[] args) {
		LinkedDisjointSet<Integer> disjointSet = new LinkedDisjointSet<Integer>();
		disjointSet.makeSet(10);
		disjointSet.makeSet(12);
		disjointSet.makeSet(13);
		disjointSet.makeSet(14);
		System.out.println(disjointSet.findSet(10));
		disjointSet.union(12, 13);
		disjointSet.union(10, 14);
		disjointSet.union(12, 13);
		System.out.println(disjointSet);

	}

}

class LinkedDisjointSet<T> {
	
	private ArrayList<LinkedList<DisjointElement<T>>> disjointSets = new ArrayList<LinkedList<DisjointElement<T>>>();
	
	public void makeSet(T elementValue){
		DisjointElement<T> disjointElement = new DisjointElement<T>(elementValue);
//		disjointElement.setRepresentative(disjointElement);
		LinkedList<DisjointElement<T>> linkedList = new LinkedList<DisjointElement<T>>();
		linkedList.add(disjointElement);
		disjointElement.setRepresentative(linkedList);
		getDisjointSets().add(linkedList);
	}
	public LinkedList<DisjointElement<T>> findSet(T elementValue){
		DisjointElement<T> element = findElement(elementValue);
		return element.getRepresentative();
	}
	
	public boolean union(T firstRepresentativeValue, T secondRepresentativeValue){
		LinkedList<DisjointElement<T>> firstRepr = findSet(firstRepresentativeValue);
		LinkedList<DisjointElement<T>> secondRepr = findSet(secondRepresentativeValue);
		if(firstRepr==null || secondRepr==null || firstRepr.equals(secondRepr)){
			return false;
		}
		if(firstRepr.size() < secondRepr.size()){
			//read like append firstRepr to secondRepr
			append(firstRepr, secondRepr);
		} else{
			append(secondRepr,firstRepr);
		}
		return true;
	}
	private void append(LinkedList<DisjointElement<T>> dataToAppend,
			LinkedList<DisjointElement<T>> appendTo) {
		appendTo.addAll(dataToAppend);
		for(DisjointElement<T> element : dataToAppend){
			element.setRepresentative(appendTo.peekFirst().getRepresentative());
		}
		getDisjointSets().remove(dataToAppend);
	}
	
	private DisjointElement<T> findElement(T elementValue){
		for(LinkedList<DisjointElement<T>> disjointSet : getDisjointSets()){
			for(DisjointElement<T> element : disjointSet){
				if(element.getValue().equals(elementValue)){
					return element;
				}
			}
		}
		return null;
	}
	
	@Override
	public String toString(){
		return getDisjointSets().toString();
	}
	public ArrayList<LinkedList<DisjointElement<T>>> getDisjointSets() {
		return disjointSets;
	}
	private void setDisjointSets(ArrayList<LinkedList<DisjointElement<T>>> disjointSets) {
		this.disjointSets = disjointSets;
	}
}

class DisjointElement<T> {
	private T value;
	private LinkedList<DisjointElement<T>> representative;
	
	public DisjointElement(T elementValue) {
		this.value=elementValue;
	}
	public T getValue() {
		return value;
	}
	public void setValue(T value) {
		this.value = value;
	}
	public LinkedList<DisjointElement<T>> getRepresentative() {
		return representative;
	}
	public void setRepresentative(LinkedList<DisjointElement<T>> representative) {
		this.representative = representative;
	}
	
	@Override
	public int hashCode() {
		final int prime = 31;
		int result = 1;
		result = prime * result + ((value == null) ? 0 : value.hashCode());
		return result;
	}
	@Override
	public boolean equals(Object obj) {
		if (this == obj)
			return true;
		if (obj == null)
			return false;
		if (getClass() != obj.getClass())
			return false;
		DisjointElement other = (DisjointElement) obj;
		if (value == null) {
			if (other.value != null)
				return false;
		} else if (!value.equals(other.value))
			return false;
		return true;
	}
	@Override
	public String toString() {
		return "DisjointElement [value=" + value + "]";
	}

}
