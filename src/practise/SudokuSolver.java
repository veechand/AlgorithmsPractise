/**
 * 
 */
package practise;

import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.regex.Pattern;

import lombok.Data;
import lombok.NonNull;

/**
 * @author veechand
 *
 */
public class SudokuSolver {

	private static final List<Integer> possibleValues = Arrays.asList(new Integer[]{1,2,3,4,5,6,7,8,9});
	/**
	 * @param args
	 * @throws IOException 
	 */
	public static void main(String[] args) throws IOException {
		SudokuSolver solver = new SudokuSolver	();
		SudokuDC sudokuMaze = new SudokuDC(9);
		BufferedReader br = new BufferedReader(new FileReader("resources/sudokumaze.input"));
		String line;
		Pattern splitter = Pattern.compile(" ");
		int xAxis = 0;
		while((line=br.readLine())!=null){
			String[] values = splitter.split(line);
			if(values.length != 9){
				System.out.println("Improper value "+line);
			}
			for(int yAxis=0;yAxis<values.length;yAxis++){
				if(!values[yAxis].equals("-")){
					sudokuMaze.setSudokuValue(xAxis, yAxis, Integer.parseInt(values[yAxis]));
				}
			}
			xAxis++;
		}
		//1st issue not given -1
		long startTime = System.nanoTime();
		solver.solveSudoku(sudokuMaze, 0, -1);
		long endTime = System.nanoTime();
		System.out.println("Time taken ="+ (endTime-startTime));
		
	}

	public void solveSudoku(SudokuDC solution, int x, int y) {
		if (isSolution(solution, x, y)) {
			processSolution(solution);
			//System.exit(0);
			solution.isSolutionFound = true;
			return;
		} else {
			y++;
			if (y >= solution.size) {
				y = 0;
				x++;
			}
			if (x >= solution.size) {
				return;
			}
			List<Integer> possibleValues = computePossibleValue(solution, x, y);
			for (int value : possibleValues) {
				solution.sudokuMaze[x][y] = value;
				//3rd issue added is possible solution
				if(isPossibleSolution(solution)){
					//System.out.printf("x=%d,y=%d,value=%d\n", x, y, value);
					solveSudoku(solution, x, y);
					if(solution.isSolutionFound){
						return;
					}
				} 
				//2nd issue didn;t revert back the value
				solution.sudokuMaze[x][y]=solution.originalSudokuMaze[x][y];
			}
		}
	}

	private boolean isPossibleSolution(SudokuDC solution) {
		return isAxisValuesUnique(solution) && isSquareValuesUnique(solution);
		
	}

	private boolean isSquareValuesUnique(SudokuDC solution) {
		List<Squares> squareBorders = solution.squareBorders;
		List<Integer> xAxis = new ArrayList<Integer>();
		//List<Integer> yAxis = new ArrayList<Integer>();
		//TODO , check only the square that is changed now
		for (Squares square : squareBorders) {
			for (int i = square.getStartPoint().getX(); i <= square
					.getEndPoint().getX(); i++) {
				for (int j = square.startPoint.y; j <= square.endPoint.y; j++) {
					if (!addIfNotExists(solution, xAxis, i, j)){
						return false;
					}
			/*		if(!addIfNotExists(solution, yAxis, j, i)){
						return false;
					}*/
				}
			}
			xAxis.clear();//yAxis.clear();
		}
		return true;
	}

	private boolean isAxisValuesUnique(SudokuDC solution) {
		List<Integer> xAxis = new ArrayList<Integer>();
		List<Integer> yAxis = new ArrayList<Integer>();
		
		for(int i=0;i<solution.size;i++){
			for(int j=0;j<solution.size;j++){
				if (!addIfNotExists(solution, xAxis, i, j)){
					return false;
				}
				if(!addIfNotExists(solution, yAxis, j, i)){
					return false;
				}
			}
			xAxis.clear();yAxis.clear();
		}
		return true;
	}

	/**
	 * @param solution
	 * @param axis
	 * @param i
	 * @param j
	 */
	private boolean addIfNotExists(SudokuDC solution, List<Integer> axis, int i,
			int j) {
		if(solution.sudokuMaze[i][j]!=0 && axis.contains(solution.sudokuMaze[i][j])){
			return false;
		} 
		axis.add(solution.sudokuMaze[i][j]);
		return true;
	}

	private boolean isSolution(SudokuDC solution, int x, int y) {
		if(x == solution.size-1 && y == solution.size-1){
			//processSolution(solution);
			return isAllConditionSatisfied(solution,x,y);
		}
		return false;
	}

	private boolean isAllConditionSatisfied(SudokuDC solution, int x, int y) {
		return isAllAxisValuesDifferent(solution)&& isAllSquaresValuesDifferent(solution);
	}

	private boolean isAllSquaresValuesDifferent(SudokuDC solution) {
		List<Squares> squareBorders = solution.squareBorders;
		int xValue = 0;
//		int yValue = 0;
		int validValue = (solution.size * (solution.size + 1)) / 2;
		for (Squares square : squareBorders) {
			for (int i = square.getStartPoint().getX(); i <= square
					.getEndPoint().getX(); i++) {
				for (int j = square.startPoint.y; j <= square.endPoint.y; j++) {
					xValue += solution.sudokuMaze[i][j];
	//				yValue += solution.sudokuMaze[j][i];
				}
			}
			//4th issue interrupted in wrong place
			if (xValue != validValue ) {
				return false;
			}
			xValue = 0;
		}
		return true;
	}

	private boolean isAllAxisValuesDifferent(SudokuDC solution) {
		int xValue = 0;int yValue = 0;
		int validValue = (solution.size * (solution.size+1))/2;
		for(int i=0;i<solution.size;i++){
			for(int j=0;j<solution.size;j++){
				xValue+=solution.sudokuMaze[i][j];
				yValue+=solution.sudokuMaze[j][i];
			}
			if(xValue != validValue || yValue != validValue){
				return false;
			}
			xValue = 0;
			yValue = 0;
		}
		return true;
	}

	private List<Integer> computePossibleValue(SudokuDC solution, int x, int y) {
		if(solution.originalSudokuMaze[x][y]!=0){
			return Arrays.asList(solution.originalSudokuMaze[x][y]);
		}
		return possibleValues;
	}

	private void processSolution(SudokuDC solution) {
		System.out.println("processing solution..");
		for(int i=0;i<solution.size;i++){
			System.out.println();
			for(int j=0;j<solution.size;j++){
				System.out.print(solution.sudokuMaze[i][j]);
				System.out.print("\t");
			}
		}
		System.out.println();
	}
}

@Data class SudokuDC {
	@NonNull int[][] sudokuMaze ;
	int[][] originalSudokuMaze;
	List<Squares> squareBorders ; 
	int size;
	boolean isSolutionFound = false;
	public SudokuDC(int size){
		sudokuMaze = new int[size][size];
		originalSudokuMaze = new int[size][size];
		this.size = size;
		squareBorders = new ArrayList<Squares>();
		for(int i=0;i<size;i=i+3){
			for(int j=0;j<size;j=j+3){
				squareBorders.add(new Squares(new SuPoint(i,j),new SuPoint(i+2,j+2)));
			}
		}
	}
	
	public void setSudokuValue(int x, int y,int value){
		sudokuMaze[x][y]=value;
		originalSudokuMaze[x][y]=value;
	}
}

@Data class Squares {
	@NonNull SuPoint startPoint;
	@NonNull SuPoint endPoint;
}

@Data class SuPoint {
	@NonNull int x;
    @NonNull int y;
}
