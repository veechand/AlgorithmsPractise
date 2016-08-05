sequence = [1,4,24,3,1,5]

longest_increasing_sequence = [ -1 for i in range(len(sequence)) ]

longest_increasing_sequence[0] = 1
for i in range(1,len(sequence)):
  if sequence[i]>sequence[i-1]:
    longest_increasing_sequence[i] = longest_increasing_sequence[i-1] + 1
  else:
    longest_increasing_sequence[i] = 1

print sequence
print max(longest_increasing_sequence)
