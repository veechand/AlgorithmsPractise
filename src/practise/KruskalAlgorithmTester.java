/**
 * 
 */
package practise;

import java.io.BufferedReader;
import java.io.File;
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;
import java.util.ArrayList;
import java.util.Collections;
import java.util.HashMap;
import java.util.LinkedList;
import java.util.List;
import java.util.Map;
import java.util.TreeSet;
import java.util.regex.Pattern;

import lombok.Data;
import lombok.EqualsAndHashCode;
import lombok.NonNull;
import lombok.ToString;

/**
 * @author veechand
 * Kruskal's algorithm to find the minimum spanning tree 
 */
public class KruskalAlgorithmTester {
	
	/**
	 * @param args
	 * @throws IOException 
	 * 
	 */
	public static void main(String[] args) throws IOException {
		List<KEdge> sortedEdges = new ArrayList<KEdge>();
		KGraph graph = new KGraph();
		BufferedReader br = new BufferedReader(new FileReader(new File("/home/moonpearl/workspace/practise/src/practise/Kruskal.input")));
		String str;
		Pattern pattern = Pattern.compile(" ");
		while((str=br.readLine())!=null){
			String[] inputs = pattern.split(str);
			KVertex vertex1 = graph.getVertex(inputs[0]);
			KVertex vertex2 = graph.getVertex(inputs[1]);
			KEdge edge1 = new KEdge(vertex1, vertex2, Integer.parseInt(inputs[2]));
			KEdge edge2 = new KEdge(vertex2, vertex1, Integer.parseInt(inputs[2]));
			vertex1.addEdge(edge1);
			vertex2.addEdge(edge2);
			sortedEdges.add(edge1);
			sortedEdges.add(edge2);
			graph.addVertex(vertex1);
			graph.addVertex(vertex2);
		}
		LinkedDisjointSet<KVertex> disjointSet = new LinkedDisjointSet<KVertex>();
		List<KVertex> vertices = graph.getVertices();
		for(KVertex vertex : vertices){
			disjointSet.makeSet(vertex);
		}
		int mst=0;
		System.out.println(sortedEdges);
		Collections.sort(sortedEdges);
		for(KEdge edge : sortedEdges){
			KVertex src = edge.getSrc();
			KVertex end = edge.getEnd();
/*			LinkedList<DisjointElement<KVertex>> srcSet = disjointSet.findSet(src);
			LinkedList<DisjointElement<KVertex>> endSet = disjointSet.findSet(end);
*/			if(disjointSet.union(src, end)){
				System.out.println(src.getName()+"->"+end.getName());
				mst+=edge.getWeight();
			}
		}
	System.out.println(disjointSet);
	System.out.println("MST="+mst);
	System.out.println("Done");	
	}

}

@Data class KGraph
{
	Map<String,KVertex> vertexCache = new HashMap<String,KVertex>();
	List<KVertex> vertices = new ArrayList<KVertex>();
	
	public KVertex getVertex(String vertex){
		KVertex vertex2 = vertexCache.get(vertex);
		if(vertex2 == null){
			vertex2 = new KVertex(vertex);
			vertexCache.put(vertex, vertex2);
		}
		return vertex2;
		
	}
	public void addVertex(KVertex vertex){
		if(!vertices.contains(vertex)){
			vertices.add(vertex);
		}
	}
}

@EqualsAndHashCode(exclude={"edges"})
@ToString(exclude={"edges"})
@Data class KVertex
{
	@NonNull String name;
	List<KEdge> edges = new ArrayList<KEdge>();
	
	public KVertex addEdge(KEdge edge){
		this.edges.add(edge);
		//for purpose of chaining
		return this;
	}
}

@Data class KEdge implements Comparable<KEdge>
{
	@NonNull KVertex src;
	@NonNull KVertex end;
	@NonNull int weight;
	@Override
	public int compareTo(KEdge o) {
		return this.weight - o.weight;
	}
}