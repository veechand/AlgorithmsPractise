/**
 * 
 */
package practise;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.HashSet;
import java.util.List;
import java.util.Map;
import java.util.Set;

import lombok.Data;
import lombok.NonNull;

/**
 * @author moonpearl
 *
 */
public class TurnsFinder {

	
	/**
	 * @param args
	 */
	public static void main(String[] args) {
		List<Point> points = new ArrayList<Point>();
		points.add(new Point(3, 4));
		points.add(new Point(3, 5));
		points.add(new Point(3, 6));
		points.add(new Point(5, 5));
		new TurnsFinder().findTurns(points);
		
		points.clear();
		points.add(new Point(0, 0));
		points.add(new Point(0, 1));
		points.add(new Point(1, 0));
		new TurnsFinder().findTurns(points);
	}

	private void findTurns(List<Point> points) {
		KeyLengthBasedOrdering dataStructure = new KeyLengthBasedOrdering();
		
		for(int i=0;i<points.size();i++){
			for(int j=i+1;j<points.size();j++){
				String slope = calulateSlope(points.get(i),points.get(j));
				Util.generalInsertion(dataStructure.data, slope, points.get(i));
				Util.generalInsertion(dataStructure.data, slope, points.get(j));
			}
		}
		int minTurns = Integer.MAX_VALUE;
		int ways = 0;
		dataStructure.populateSortedMap();
		//iterating through sortedMap. Keys are the values of slopes
		//TODO: Confirms that it returns in decreasing order
		for(Set<String> slopesWithEqualNumberOfPoints : dataStructure.sortedMap.values()){
			for(String slope : slopesWithEqualNumberOfPoints){
				Set<Point> collinearPoints = dataStructure.data.get(slope);
				int turns = findTurns(collinearPoints,1,slope,points,dataStructure); 
				if(turns<minTurns){
					minTurns = turns;
					ways=1;
				} else if (turns==minTurns){
					ways++;
				}
			}
		}
		System.out.println("Minimum Number of Turns = "+minTurns);
		System.out.println("Number of ways = "+ways*2);
	}

	private int findTurns(Set<Point> currentCollinearPoints, int turns,
			String currentSlope, List<Point> points,
			KeyLengthBasedOrdering dataStructure) {
		if (currentCollinearPoints.size() >= points.size() - 2) {
			return turns + 1;
		}
		int maxFound=Integer.MIN_VALUE;String maxKey="";
		for (Set<String> slopesWithEqualNumberOfPoints : dataStructure.sortedMap
				.values()) {
			for (String slope : slopesWithEqualNumberOfPoints) {
				/*if(slope.equals(currentSlope)){
					continue;
				}*/
				Set<Point> collinearPoints = dataStructure.data.get(slope);
				int numberFound=0;
				for(Point point : collinearPoints){
					if(!currentCollinearPoints.contains(point)){
						numberFound++;
					}
				}
				if(numberFound>maxFound){
					maxFound=numberFound;
					maxKey=slope;
				}
				if(maxFound+currentCollinearPoints.size()>=points.size()-2){
					currentCollinearPoints.addAll(dataStructure.data.get(maxKey));
					return turns+=findTurns(currentCollinearPoints, turns, currentSlope, points, dataStructure);
				}
			}
		}
		currentCollinearPoints.addAll(dataStructure.data.get(maxKey));
		return turns+=findTurns(currentCollinearPoints, turns, currentSlope, points, dataStructure);
	}

	private String calulateSlope(Point point1, Point point2) {
			return String.valueOf(((point2.getY()-point1.getY())/(point2.getX()-point1.getX())));
	}

}

class KeyLengthBasedOrdering {
	Map<String,Set<Point>> data = new HashMap<String, Set<Point>>();
	Map<Integer,Set<String>> sortedMap = new HashMap<Integer,Set<String>>();
	
	public void populateSortedMap(){
		for(String slopeValue : data.keySet()){
			Util.generalInsertion(sortedMap, data.get(slopeValue).size(),slopeValue);
		}
	}
}

 final class Util {
	public static <T,V> void generalInsertion(Map<T,Set<V>> sourceMap,T key, V value){
		Set<V> currentSet = sourceMap.get(key);
		if(currentSet == null){
			currentSet = new HashSet<V>();
			sourceMap.put(key, currentSet);
		}
		currentSet.add(value);
	}
}

@Data  class Point 
{
	@NonNull float x;
	@NonNull float y;
}
 