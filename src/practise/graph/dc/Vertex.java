/**
 * 
 */
package practise.graph.dc;

import java.util.ArrayList;
import java.util.List;

import lombok.Data;
import lombok.EqualsAndHashCode;
import lombok.NonNull;
import lombok.ToString;

/**
 * @author veechand
 * 
 */
@EqualsAndHashCode(exclude = { "outgoingEdges", "distance", "parentVertex",
		"startTime", "endTime", "vertexState" })
@ToString(exclude = { "outgoingEdges", "distance", "parentVertex",
		"startTime", "endTime", "vertexState"  })
@Data
public class Vertex implements Comparable<Vertex> {
	@NonNull
	private String nodeName;
	private List<Edge> outgoingEdges = new ArrayList<Edge>();
	/*
	 * Distance can be used represent dfs depth, shortest distance and
	 * accordingly the parentVertex changes
	 */
	private int distance;
	private Vertex parentVertex;

	private VertexState vertexState = null;

	private int startTime;
	private int endTime;

	@Override
	public int compareTo(Vertex other) {
		return this.distance - other.distance;
	}

	public void addEdge(Edge edge) {
		this.outgoingEdges.add(edge);

	}

}
