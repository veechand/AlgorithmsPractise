/**
 * 
 */
package practise.graph;

import practise.graph.dc.Edge;
import practise.graph.dc.Graph;

/**
 * @author veechand
 *
 */
public interface EdgeProcessor {
	
	public void processEdge(Edge edge, Graph graph);

}
