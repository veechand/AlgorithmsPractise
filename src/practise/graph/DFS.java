/**
 * 
 */
package practise.graph;

import java.util.List;

import practise.graph.dc.Edge;
import practise.graph.dc.EdgeType;
import practise.graph.dc.Graph;
import practise.graph.dc.Vertex;
import practise.graph.dc.VertexState;

/**
 * @author veechand
 *
 */
public class DFS implements EdgeProcessor {

	
	private int time = 0;
	/**
	 * @param args
	 */
	public static void main(String[] args) {
		Graph graph = Graph.buildGraph("resources/dfs.input");
		DFS dfs = new DFS();
		dfs.doDFS(graph.getVertex("w"), graph,dfs);
		List<Vertex> vertices = graph.getVertices();
		for(Vertex v : vertices){
			System.out.println(v.getNodeName()+" "+v.getStartTime()+"/"+v.getEndTime());
		}
		
	}
	//will look only thrrough one connected component 
	public void doDFS(Vertex source,Graph graph, EdgeProcessor edgeProcessor){
		source.setVertexState(VertexState.DISCOVERED);
		source.setStartTime(time++);
		List<Edge> edges = source.getOutgoingEdges();
		for(Edge edge : edges){
			Vertex end = edge.getEnd();
			edgeProcessor.processEdge(edge,graph);
			if(end.getVertexState() == null){
				end.setParentVertex(source);
				doDFS(end,graph,edgeProcessor);
			}
		}
		source.setVertexState(VertexState.PROCESSED);
		source.setEndTime(time++);
	}

	@Override
	public void processEdge(Edge edge,Graph graph) {
		Vertex src = edge.getSrc();
		Vertex end = edge.getEnd();

		if (end.getVertexState() == VertexState.DISCOVERED
				&& end.getVertexState() != VertexState.PROCESSED) {
			System.out.println("Detected Back edge "+edge);
			//return EdgeType.BACK;
		}

		if (end.getVertexState() == null) {
			System.out.println("Detected Tree edge "+edge);
			//return EdgeType.TREE;
		}

		if (end.getVertexState() == VertexState.PROCESSED
				&& end.getStartTime() > src.getStartTime()) {
			System.out.println("Detected Forward edge "+edge);
			//return EdgeType.FORWARD;
		}

		 if(end.getVertexState() == VertexState.PROCESSED &&
		 end.getStartTime() < src.getStartTime()){
			 System.out.println("Detected cross edge "+edge);
			 //return EdgeType.CROSS;
		 }
	}
}
