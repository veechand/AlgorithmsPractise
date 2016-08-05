# =========== backtracking solution starts ===========

input_sequence = [ 1,3,5 ]
_sum = 11

input_sequence = [ 5,5,5,15 ]
_sum = 15

input_sequence = [ 1,2,3 ]
_sum = 0

output = []

def all_possible_sequence(cur_sum, sequence):
  if cur_sum < 0 or cur_sum > _sum:
    return
  if is_solution(cur_sum):
    #print "Solution..."
    result = ",".join(map(lambda x: str(x), sequence))
    if result not in output:
      output.append(result) 
    #print len(sequence), sum(sequence)
    pass
  else:
    all_possible_solution = get_all_possible_solution(cur_sum)
    for solution in all_possible_solution:
      cur_sum += solution
      # sequence.append(solution)
      a = sequence + [solution]
      all_possible_sequence(cur_sum,a)
      cur_sum -= solution
      # sequence = sequence[0:-1]

def is_solution(cur_sum):
  # print cur_sum, _sum
  return cur_sum == _sum

def get_all_possible_solution(cur_sum):
  all_possible_solution = []
  for i in input_sequence:
      if cur_sum + i <= _sum:
        all_possible_solution.append(i)
  return all_possible_solution


# all_possible_sequence(0,[])
# print output

# =========== backtracking solution ends ===========



# DP

input_sequence = [ 1,3,5 ]
_sum = 11
all_sum=[1000000 for i in range(_sum+1)]
all_sum[0] = 0
for all_sum_index in range(_sum+1):
  for _input in input_sequence:
    if _input <= all_sum_index and all_sum[all_sum_index -_input]+1 < all_sum[all_sum_index]:
        all_sum[all_sum_index] = all_sum[all_sum_index -_input]+1 
print all_sum
print all_sum[-1]

















