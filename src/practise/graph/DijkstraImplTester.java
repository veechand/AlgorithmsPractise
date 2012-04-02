/**
 * 
 */
package practise.graph;

import java.util.List;

import practise.MinHeap;
import practise.graph.dc.Edge;
import practise.graph.dc.Graph;
import practise.graph.dc.Vertex;

/**
 * @author veechand
 *
 */
public class DijkstraImplTester {
	
	public static void main(String args[]) throws Exception{
		
		Graph graph = Graph.buildGraph("resources/Dijkstra.input");
		DijkstraImplTester dijkstra = new DijkstraImplTester();
		dijkstra.findShortestDistance(graph.getVertex("s"), graph);
		
		List<Vertex> vertices = graph.getVertices();
		for(Vertex v : vertices){
			System.out.println("Name="+v.getNodeName()+" Distance="+v.getDistance());
		}
	}
	
	public void findShortestDistance(Vertex source, Graph graph){
		List<Vertex> vertices = graph.getVertices();
		MinHeap<Vertex> queue = new MinHeap<Vertex>();
		for(Vertex v : vertices){
			if(v.equals(source)){
				continue;
			}
			v.setDistance(Integer.MAX_VALUE);
			queue.add(v);
		}
		source.setDistance(0);
		queue.add(source);
		
		while(!queue.empty()){
			Vertex currentVertex = queue.deleteMin();
			int currentVertexDistance = currentVertex.getDistance();
			List<Edge> outgoingEdges = currentVertex.getOutgoingEdges();
			for(Edge edge : outgoingEdges){
				Vertex end = edge.getEnd();
				int endDistance = end.getDistance();
				if(endDistance > currentVertexDistance+edge.getWeight()){
					end.setDistance(currentVertexDistance+edge.getWeight());
					end.setParentVertex(currentVertex);
					queue.minHeapify(queue.size());
				}
			}
		}
		
	}

}
