/**
 * 
 */
package practise.graph.dc;

import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.regex.Pattern;

import lombok.Data;

/**
 * @author veechand
 *
 */
@Data public class Graph {
	
	private Map<String ,Vertex> vertexCache = new HashMap<String,Vertex>();
	
	private List<Vertex> vertices = new ArrayList<Vertex>();
	
	private boolean directed = false;

	private int vertexCount; 
	private int edgeCount; 
	
	public Vertex getVertex(String name){
		Vertex vertex = vertexCache.get(name);
		if(vertex == null){
			vertex = new Vertex(name);
			vertexCache.put(name, vertex);
		}
		return vertex;
	}
	
	public void addVertex(Vertex vertex){
		if(!vertices.contains(vertex)){
			vertices.add(vertex);
		}
	}

	/*
	 * The first two lines will have the count number of vertex and number of edges 
	 * This is how the data file for bandwidth problem is formatted
	 */
	public static Graph buildGraphVertexAndEdgeCount(String fileName) {
		Graph graph = new Graph();
		try {
			BufferedReader br = new BufferedReader(new FileReader(fileName));
			graph.setVertexCount(Integer.parseInt(br.readLine().trim()));
			graph.setEdgeCount(Integer.parseInt(br.readLine().trim()));
			buildVertexAndEdges(graph, br);
		} catch (IOException ie) {
			ie.printStackTrace();
			graph = new Graph();
		}
		return graph;
	}

	
	public static Graph buildGraph(String fileName) {
		Graph graph = new Graph();
		try {
			BufferedReader br = new BufferedReader(new FileReader(fileName));
			String line = br.readLine();
			if ("directed".equalsIgnoreCase(line)) {
				graph.setDirected(true);
			}
			buildVertexAndEdges(graph, br);
		} catch (IOException ie) {
			ie.printStackTrace();
			graph = new Graph();
		}
		return graph;
	}

	/**
	 * @param graph
	 * @param br
	 * @param pattern
	 * @return
	 * @throws IOException
	 */
	private static void buildVertexAndEdges(Graph graph, BufferedReader br) throws IOException {
		String line;
		Pattern pattern = Pattern.compile("\\s{1,4}");
		while ((line = br.readLine()) != null) {
			String[] split = pattern.split(line);
			Vertex src = graph.getVertex(split[0]);
			Vertex end = graph.getVertex(split[1]);
			// for unweighted graph every graph will be of weight 0
			int weight = 0;
			if (split.length == 3) {
				weight = Integer.parseInt(split[2].trim());
			}
			src.addEdge(new Edge(src, end, weight));
			if (!graph.isDirected()) {
				end.addEdge(new Edge(end, src, weight));
			}
			graph.addVertex(src);
			graph.addVertex(end);
		}
	}
	
	@Override
	public String toString(){
		StringBuilder output = new StringBuilder();
		List<Vertex> vertices = getVertices();
		int totalWeight = 0;
		for(Vertex v : vertices){
			output.append("Edges outgoing from vertex "+v.getNodeName()+" are ");
			List<Edge> outgoingEdges = v.getOutgoingEdges();
			for(Edge e : outgoingEdges){
				output.append(e.getEnd().getNodeName()+",");
				totalWeight+=e.getWeight();
			}
			output.append("\n");
		}
		output.append("Total weight ="+totalWeight/2);
		return output.toString();
	}
}
