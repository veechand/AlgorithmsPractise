package practise.graph;

import java.util.ArrayList;
import java.util.List;

import practise.graph.dc.Edge;
import practise.graph.dc.Graph;
import practise.graph.dc.Vertex;

/**
 * @author veechand
 * 
 */
public class BandwidthCalculator {

	private int resultBandwidth = Integer.MAX_VALUE;
	private List<Vertex> efficientSolution = null;
	
	public static void main(String[] args){
		BandwidthCalculator bandwidthCalculator = new BandwidthCalculator();
		args = new String[1];
		args[0]="resources/bandwidth.input";
		Graph graph = Graph.buildGraphVertexAndEdgeCount(args[0]);
		bandwidthCalculator.bandwidth(graph, new ArrayList<Vertex>(graph.getVertices().size()), 0, Integer.MIN_VALUE);
		System.out.println("Bandwidth="+bandwidthCalculator.resultBandwidth);
		System.out.println("Permutation="+bandwidthCalculator.efficientSolution);
	}
	
	public void bandwidth(Graph graph, List<Vertex> solution, int position, int bandwidth){
		if(isSolution(graph,position)){
			processSolution(solution,bandwidth);
		}
		else {
		//	position++;
			List<Vertex> values = getAllPossibleValues(graph);
			for(Vertex value : values){
				//solution.add(position, value);
				solution.add(value);
				int currentBandwidth = calculateNewBandwidth(solution);
				if(currentBandwidth!=-1){
					if(currentBandwidth > bandwidth){
						bandwidth=currentBandwidth;
					}
					position++;
					bandwidth(graph,solution,position,bandwidth);
					solution.remove(solution.size()-1);
					position--;

				} else {
					solution.remove(solution.size()-1);
				}
			}
		}
	}

	/*
	 * Check is the passed solution could be a possible end solution.
	 * returns the longestBandwidth with this possible solution else -1 if not a possible
	 * solution 
	 *  Possible Solution :
	 *     - This is a new vertex
	 *     - The longest path for the newly added vertex to all the avbl edges is not greater than 
	 * 		 already calculated bandwidth
	 */
	private int calculateNewBandwidth(List<Vertex> solution) {
		Vertex newlyAddedVertex = solution.get(solution.size()-1);
		if(solution.indexOf(newlyAddedVertex) != solution.size()-1){
			//the vertex is already added to the solution
			return -1;
		}
		/*
		 * This variable is used to maintain the maximum distance of this newly
		 * added vertex to any of the already added vertex. The distance will be
		 * calculated only if there is an edge
		 */
		int currentVertexBandwidth=Integer.MIN_VALUE;
		List<Edge> edges = newlyAddedVertex.getOutgoingEdges();
		for(Edge edge : edges){
			Vertex end = edge.getEnd();
			int endsPositionInSolution = solution.indexOf(end);
			if(endsPositionInSolution != -1){
				//means the end is already added to the solution
				int bandwidthBetweenCurrentVertexAndEnd = (solution.size()-1)-endsPositionInSolution;
				if(bandwidthBetweenCurrentVertexAndEnd > resultBandwidth){
					// this bandwidth is more, so putting current vertex here is not an efficient solution
					return -1;
				}
				else if(bandwidthBetweenCurrentVertexAndEnd > currentVertexBandwidth){
					currentVertexBandwidth = bandwidthBetweenCurrentVertexAndEnd;
				}
			}
		}
		return currentVertexBandwidth;
	}

	private List<Vertex> getAllPossibleValues(Graph graph) {
		return graph.getVertices();
	}

	private void processSolution(List<Vertex> solution, int bandwidth) {
		if(bandwidth<resultBandwidth){
			resultBandwidth=bandwidth;
			efficientSolution=new ArrayList<Vertex>(solution);
		}
		
	}

	private boolean isSolution(Graph graph, int position) {
		return position == graph.getVertexCount();
	}
}













