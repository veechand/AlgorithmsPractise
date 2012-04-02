/**
 * 
 */
package practise;

/**
 * @author veechand
 * To realize the power of dynamic programming 
 */
public class Fibonnacci {

	
	/**
	 * @param args
	 */
	public static void main(String[] args) {
		Fibonnacci fibonnacci = new Fibonnacci();
		long result=-1;
		if(args[0].equalsIgnoreCase("dynamic")){
			result=fibonnacci.calculateFibUsingDynamicProg(Integer.parseInt(args[1]));
		} else {
			result=fibonnacci.calculateFib(Integer.parseInt(args[1]));
		}
		System.out.println("Result="+result);
	}

	private long calculateFib(int number) {
		if(number==1){
			return 1;
		}
		else if(number==2){
			return 2;
		}
		return calculateFib(number-1)+calculateFib(number-2);
	}

	private long calculateFibUsingDynamicProg(int number) {
		long[] resultArray=new long[number];
		resultArray[0]=1;
		resultArray[1]=2;
		int start = 3;
		while(start<=number){
			resultArray[start-1]=resultArray[start-2]+resultArray[start-3];
			start++;
		}
		return resultArray[number-1];
	}

}
