/**
 * 
 */
package practise;

import java.util.ArrayList;
import java.util.List;

import lombok.Data;
import lombok.NonNull;

/**
 * @author veechand
 *
 */
public class TaskExecutionTester {

	private int minDeviation = Integer.MAX_VALUE;
	private List<Integer> minDeviationTaskIDs=new ArrayList<Integer>();
	private int totalMinutesNeeded=0;
	/**
	 * @param args
	 */
	public static void main(String[] args) {
		//processSolution();
		//new Task(deadline, minute, id)
		Task task1 = new Task(2, 2, 1);
		Task task2 = new Task(1, 1, 2);
		Task task3 = new Task(4, 3, 3);
		Task task4 = new Task(10, 1, 4);
		Task task5 = new Task(2, 1, 5);
		
		List<Task> userInputTask = new ArrayList<Task>();
		
		userInputTask.add(task1);
		userInputTask.add(task2);
		userInputTask.add(task3);
		userInputTask.add(task4);
		userInputTask.add(task5);
		
		TaskExecutionTester taskExecutionTester = new TaskExecutionTester();
		
		for(Task task : userInputTask){
			taskExecutionTester.totalMinutesNeeded+=task.getMinute();
		}
		
		taskExecutionTester.backtrack(new Task[taskExecutionTester.totalMinutesNeeded],-1,userInputTask);
		taskExecutionTester.processSolution();
	}

	/**
	 * Backtrack.
	 *
	 * @param taskArray, Will contain the list of tasks that is going to be executed at ith min. A task at i means, it will be 
	 * executed at ith min
	 * @param k the current processing position
	 * @param userInputTasks the user input tasks
	 */
	public void backtrack(Task[] taskArray, int k, List<Task> userInputTasks) {
		if (isSolution(taskArray, userInputTasks, k)) {
			//procejssSolution();
		} else {
			k++;
			List<Task> taskApplicableAtThisMin = construct(taskArray, k,
					userInputTasks);
			for (Task task : taskApplicableAtThisMin) {
				taskArray[k] = task;
				if (isCorrectCombination(taskArray, userInputTasks)) {
					backtrack(taskArray, k, userInputTasks);
				}
				taskArray[k]=null;
			}
		}
	}

	/**
	 * Can the task be executed at the ith min. 
	 * taskArray[i] will have task that is going to be executed at ith min. However taskArray.minutes = 1 and 
	 * taskArray[i-j], for some arbitary value of j, might contain the same task. In this case the combination is wrong  
	 * @param taskArray the task array
	 * @param userInputTasks the user input tasks
	 * @return true, if is correct combination
	 */
	private boolean isCorrectCombination(Task[] taskArray,
			List<Task> userInputTasks) {
		/*
		 *  The number of times the task has been executed as per taskArray
		 */
		int[] executedTimes = new int[totalMinutesNeeded];
		for(Task task: taskArray){
			if(task == null){
				continue;
			}
			executedTimes[task.getId()-1]+=1;
			if(executedTimes[task.getId()-1]>task.getMinute()){
				return false;
			}
		}
		return true;
	}

	/**
	 * Construct the possible list of tasks that can be executed at any given minute.
	 *
	 * @param taskArray the task array
	 * @param k the k
	 * @param userInputTasks the user input tasks
	 * @return the list
	 */
	private List<Task> construct(Task[] taskArray, int k,
			List<Task> userInputTasks) {
		List<Task> possibleCombination = new ArrayList<Task>();
		for(Task task : userInputTasks){
			for(int i=0;i<task.getMinute();i++){
				possibleCombination.add(task);
			}
		}
		return possibleCombination;
	}

	/**
	 * Just believed that the solution is reached, so processing it
	 */
	private void processSolution() {
		System.out.println("Minimum deviation="+minDeviation);
		System.out.println("Task execution order="+minDeviationTaskIDs);
	}

	/**
	 * Checks if is solution.
	 *
	 * @param taskArray the task array
	 * @param userInputTask the user input task
	 * @param k the k
	 * @return true, if is solution
	 */
	private boolean isSolution(Task[] taskArray, List<Task> userInputTask, int k) {
	
		if(k==totalMinutesNeeded-1){
			calculate(taskArray,userInputTask);
		}
		return k==totalMinutesNeeded-1;
		//return false;
	}

	/**
	 * Calculate the current minimum and adjust the global minimum
	 *
	 * @param taskArray the task array
	 * @param userInputTask the user input task
	 */
	private void calculate(Task[] taskArray, List<Task> userInputTask) {
		int i=1;
		for(Task task : taskArray){
			task.setCompletionTime(i++);
		}
		int maxDeviation=Integer.MIN_VALUE;
		for(Task task : taskArray){
			int deviation = task.getCompletionTime()-task.getDeadline();
			if(deviation>maxDeviation){
				maxDeviation=deviation;
			}
		}
		if(maxDeviation<minDeviation){
			minDeviation=maxDeviation;
			minDeviationTaskIDs.clear();
			for(Task task : taskArray){
				minDeviationTaskIDs.add(task.getId());
			}
		}
	}
}


@Data class Task
{
	@NonNull int deadline;
	@NonNull int minute;
	@NonNull int id;
	int completionTime=-1;
}