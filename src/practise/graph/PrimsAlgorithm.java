/**
 * 
 */
package practise.graph;

import java.util.List;

import practise.MinHeap;
import practise.graph.dc.Edge;
import practise.graph.dc.Graph;
import practise.graph.dc.Vertex;
import practise.graph.dc.VertexState;

/**
 * @author veechand
 * 
 * Implementation of PrimsAlgorithm 
 *
 */
public class PrimsAlgorithm implements EdgeProcessor {

	/**
	 * @param args
	 */
	public static void main(String[] args) {
		Graph graph = Graph.buildGraph("resources/prims.input");
		PrimsAlgorithm mstFinder = new PrimsAlgorithm();
		Graph mstGraph = mstFinder.findMST(graph);
		System.out.println(mstGraph);	
		//adding one othe edge
		Vertex cVertex = mstGraph.getVertex("c");
		Vertex hVertex = mstGraph.getVertex("h");
		int newEdgeWeight = 1;
		hVertex.addEdge(new Edge(hVertex,cVertex,newEdgeWeight));
		cVertex.addEdge(new Edge(cVertex,hVertex,newEdgeWeight));
		DFS dfs = new DFS();
		dfs.doDFS(mstGraph.getVertices().get(0), mstGraph,mstFinder);
		if(mstFinder.maxEdge.getWeight() > newEdgeWeight){
			Vertex src = mstFinder.maxEdge.getSrc();
			Vertex end = mstFinder.maxEdge.getEnd();
			src.getOutgoingEdges().remove(mstFinder.maxEdge);
			end.getOutgoingEdges().remove(new Edge(end,src,mstFinder.maxEdge.getWeight()));
		} else {
			hVertex.getOutgoingEdges().remove(new Edge(hVertex,cVertex,newEdgeWeight));
			cVertex.getOutgoingEdges().remove(new Edge(hVertex,cVertex,newEdgeWeight));
		}
		//System.out.println("Found Max Edge "+mstFinder.maxEdge);
		System.out.println(mstGraph);
	}

	private Edge maxEdge = null;
	
	public Graph findMST(Graph graph){
		Graph mstGraph = new Graph();
		mstGraph.setDirected(graph.isDirected());
		
		MinHeap<Edge> queue = new MinHeap<Edge>();
		Vertex randomSource = graph.getVertices().get(0);
		mstGraph.addVertex(mstGraph.getVertex(randomSource.getNodeName()));
		List<Edge> outgoingEdges = randomSource.getOutgoingEdges();
		for(Edge edge : outgoingEdges){
			queue.add(edge);
		}
		while(!queue.empty()){
			Edge minEdge = queue.deleteMin();
			if(!mstGraph.getVertices().contains(minEdge.getEnd())){
				//mstGraph.addVertex(minEdge.getEnd());
				Vertex mstSrc = mstGraph.getVertex(minEdge.getSrc().getNodeName());
				Vertex mstEnd = mstGraph.getVertex(minEdge.getEnd().getNodeName());
				mstSrc.addEdge(new Edge(mstSrc,mstEnd,minEdge.getWeight()));
				if(!graph.isDirected()){
					mstEnd.addEdge(new Edge(mstEnd,mstSrc,minEdge.getWeight()));
				}
				//jmstGraph.addVertex(mstSrc);
				mstGraph.addVertex(mstEnd);
				
				List<Edge> outGoingEdgesFromEnd = minEdge.getEnd().getOutgoingEdges();
				for(Edge e1: outGoingEdgesFromEnd){
					queue.add(e1);
				}
			}
		}
		return mstGraph;
	}

	@Override
	public void processEdge(Edge edge, Graph graph) {
		Vertex src = edge.getSrc();
		Vertex end = edge.getEnd();
		// src.getParentVertex().equals(end) this check is not needed if only one edge is stored even for undirected graph
		if(end.getVertexState() == VertexState.DISCOVERED && end.getVertexState() != VertexState.PROCESSED && !src.getParentVertex().equals(end)){
			System.out.println("Detected Back edge, finding MaxEdge "+edge);
			if(maxEdge != null){
				System.out.println("WARN:Some issue.. y prims graph shows two back edge on addition on one node");
			}
			maxEdge  = findMaxEdge(src, end);
			System.out.println("Found maxEdge "+maxEdge);
			/*graph.getVertex(maxEdge.getSrc().getNodeName()).getOutgoingEdges().remove(maxEdge);
			if(!graph.isDirected()){
				graph.getVertex(maxEdge.getEnd().getNodeName())
						.getOutgoingEdges()
						.remove(new Edge(maxEdge.getEnd(), maxEdge.getSrc(),
								maxEdge.getWeight()));
			}*/
		}
	}

	/**  
	 * @param src
	 * @param end
	 */
	private Edge findMaxEdge(Vertex src, Vertex end) {
		Edge maxEdge = null;
		int maxWeight = Integer.MIN_VALUE;
		Vertex realEnd = end;
		while(!src.equals(realEnd)){
			Edge currentEdge = null;
			List<Edge> outgoingEdges = src.getOutgoingEdges();
			for(int i=0;i<outgoingEdges.size();i++){
				currentEdge = outgoingEdges.get(i);
				if(!currentEdge.getEnd().equals(end)){
					break;
				}
			}
			int currentEdgeWeight = currentEdge.getWeight();
			if(currentEdgeWeight > maxWeight){
				maxWeight = currentEdgeWeight;
				maxEdge = currentEdge;
			}
			end = src;
			src = src.getParentVertex();
		}
		return maxEdge;
	}

}
