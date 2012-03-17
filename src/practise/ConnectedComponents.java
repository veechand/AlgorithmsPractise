/**
 * 
 */
package practise;

/**
 * @author moonpearl
 * This is to use link disjoint set and form connected components
 */
public class ConnectedComponents {

	/**
	 * @param args
	 */
	public static void main(String[] args) {
		LinkedDisjointSet<String> disjointSet = new LinkedDisjointSet<String>();
		disjointSet.makeSet("a");
		disjointSet.makeSet("b");
		disjointSet.makeSet("c");
		disjointSet.makeSet("d");
		disjointSet.makeSet("e");
		disjointSet.makeSet("f");
		disjointSet.makeSet("g");
		disjointSet.makeSet("h");
		disjointSet.makeSet("i");
		disjointSet.makeSet("j");
		disjointSet.union("a", "b");
		disjointSet.union("a", "c");
		disjointSet.union("c", "b");
		disjointSet.union("d", "b");
		disjointSet.union("e", "f");
		disjointSet.union("e", "g");
		disjointSet.union("h", "i");
		System.out.println(disjointSet);
		System.out.println("Number of Connected Components="+disjointSet.getDisjointSets().size());

	}

}
