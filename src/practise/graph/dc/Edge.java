/**
 * 
 */
package practise.graph.dc;

import lombok.Data;
import lombok.NoArgsConstructor;
import lombok.NonNull;

/**
 * @author veechand
 *
 */
@Data public class Edge implements Comparable<Edge> {
	@NonNull private Vertex src;
	@NonNull private Vertex end;
	@NonNull private int weight;
	@Override
	public int compareTo(Edge other) {
		return this.weight - other.weight;
	}

}
