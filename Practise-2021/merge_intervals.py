"""
[[1,3],[2,5]]
[[1,5]]
1. Are these intervals sorted on the start time
[2,7] [5,10] [12,15] [14,19]
[2,7] [9-15] [6-11] 
2-11
If the intervals are sorted on starting range
while(i<len(intervals)-2):
  if intervals[i][end] >= intervals[i+1][start]:
      intervals[i] = [intrtls[i][start][intervals[i+1][end]]
        intervals.pop(intervals[i+1])
[2-9] [5-9]
"""
class Solution(object):
    
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        INTERVAL_START = 0
        INTERVAL_END = 1
        index = 0
        length = len(intervals) - 1
        sortedIntervals = sorted(intervals, key=lambda x: x[0])
        while (index < length):
            if (sortedIntervals[index][INTERVAL_END] >= sortedIntervals[index + 1][INTERVAL_START]):
                end = max(sortedIntervals[index + 1][INTERVAL_END], sortedIntervals[index][INTERVAL_END])
                sortedIntervals[index] = [sortedIntervals[index][INTERVAL_START], end]
                sortedIntervals.pop(index+1)
                length -= 1
            else:
                index = index + 1
        return sortedIntervals

if __name__ == "__main__":
    testCases = [ 
    ([[2,7],[9,15],[6,11]],[[2,15]]),
    ([[1,4],[2,3]],[[1,4]])
    ]
    