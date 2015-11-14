/**
 * 
 */
package practise;

import java.util.HashMap;
import java.util.Map;

/**
 * @author veechand
 *
 */
public class TreeDisjointSetTester {

	/**
	 * @param args
	 */
	public static void main(String[] args) {
		TreeDisjointSet<Integer> disjointSet = new TreeDisjointSet<Integer>();
		disjointSet.makeSet(10);
		disjointSet.makeSet(12);
		disjointSet.makeSet(13);
		disjointSet.makeSet(14);
		System.out.println(disjointSet.findSet(10));
		System.out.println(disjointSet);
		disjointSet.union(12, 13);
		System.out.println(disjointSet);
		disjointSet.union(10, 14);
		System.out.println(disjointSet);
		disjointSet.union(12, 14);
		System.out.println(disjointSet);
		System.out.println("Done");
//		System.out.println(disjointSet);
	}

}

class TreeDisjointSet<T>{
	Map<T,DisjointTreeElement<T>> disjointSetElements = new HashMap<T,DisjointTreeElement<T>>();
	public void makeSet(T elementValue){
		DisjointTreeElement<T> disjointElement = new DisjointTreeElement<T>(elementValue);
		disjointElement.setParent(disjointElement);
		disjointSetElements.put(disjointElement.getValue(),disjointElement);
	}
	public DisjointTreeElement<T> findSet(T elementValue){
		return findSet(findElement(elementValue));
	}
	
	private DisjointTreeElement<T> findSet(DisjointTreeElement<T> findElement) {
		if(findElement.getParent().equals(findElement)){
			return findElement;
		}
		findElement.setParent(findSet(findElement.getParent()));
		return findElement.getParent(); //path-compression
		
	}
	private DisjointTreeElement<T> findElement(T elementValue) {
		for(DisjointTreeElement<T> element : disjointSetElements.values()){
			DisjointTreeElement<T> previousElement = null;
			while(previousElement == null || !element.equals(previousElement)){
				if(element.getValue().equals(elementValue)){
					return element;
				}
				previousElement = element;
				element = element.getParent();
			}
		}
		return null;
	}
	
	public void union(T x, T y){
		DisjointTreeElement<T> xSet = findSet(x);
		DisjointTreeElement<T> ySet = findSet(y);
		disjointSetElements.remove(xSet.getValue());
		disjointSetElements.remove(ySet.getValue());
		if(xSet.getRank() > ySet.getRank()){
			ySet.setParent(xSet.getParent());
			disjointSetElements.put(xSet.getParent().getValue(),ySet);
		} else {
			xSet.setParent(ySet.getParent());
			disjointSetElements.put(ySet.getParent().getValue(),xSet);
		}
		if(xSet.getRank() == ySet.getRank()){
			ySet.incrementRank();
		}
		
	}
	
	@Override
	public String toString(){
		for(DisjointTreeElement<T> element : disjointSetElements.values()){
			DisjointTreeElement<T> previousElement = null;
			System.out.println();
			while(previousElement == null || !element.equals(previousElement)){
				System.out.print(element.getValue()+",");
				previousElement = element;
				element = element.getParent();
			}
		}
		return "";//disjointSetElements.toString();
	}
}
class DisjointTreeElement<T> {
	private T value;
	private DisjointTreeElement<T> parent;
	private int rank=0; //union by rank
	
	public DisjointTreeElement(T elementValue) {
		this.value = elementValue;
	}

	public void incrementRank(){
		setRank(getRank() + 1);
	}

	public T getValue() {
		return value;
	}

	public void setValue(T value) {
		this.value = value;
	}

	public DisjointTreeElement<T> getParent() {
		return parent;
	}

	public void setParent(DisjointTreeElement<T> parent) {
		this.parent = parent;
	}

	public int getRank() {
		return rank;
	}

	public void setRank(int rank) {
		this.rank = rank;
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
		DisjointTreeElement other = (DisjointTreeElement) obj;
		if (value == null) {
			if (other.value != null)
				return false;
		} else if (!value.equals(other.value))
			return false;
		return true;
	}

	@Override
	public String toString() {
		return "DisjointTreeElement [value=" + value 
				+ ", rank=" + rank + "]";
	}
}