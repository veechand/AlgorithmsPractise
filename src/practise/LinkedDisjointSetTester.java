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

