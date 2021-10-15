letter_order = "abcdefghijklmnop"
word_list = ["ab","abc","hij"]


def is_words_sorted(word1, word2,words_in_pos):
	i = 0
	j = 0
	while (i<len(word1) and j<len(word2)):
		if(words_in_pos[word1[i]]<words_in_pos[word2[j]]):
			return True
		if(words_in_pos[word1[i]]>words_in_pos[word2[j]]):
			return False
		if(words_in_pos[word1[i]] == words_in_pos[word2[j]]):
			i+=1
			j+=1
	if(len(word1)<=len(word2)):
		return True
	else:
		return False


def ordering_words_in_pos(letter_order):
	return_value = {}
	i = 0
	for l in letter_order:
		return_value[l] = i
		i += 1
	return return_value


word_count = 0
words_in_pos = ordering_words_in_pos(letter_order)

while word_count < len(word_list) - 1:
	output = is_words_sorted(word_list[word_count], word_list[word_count+1], words_in_pos)
	if not output:
		print "Not orderered"
		break
	word_count += 1

if output:
	print "Ordered"

i=0
unsorted_output = []
while(i<len(s)):
	k = s[i:i+1000]
	i+=1000
	unsorted_output.append(k)

sorted_list_output = []
for o in unsorted_output:
	sorted_list_output.append(sorted(o))

def sort_with_efficient_memory(to_sort_list):
	if(len(to_sort_list) == 1):
		return to_sort_list
	output = sorted_two_arrays(to_sort_list[0],to_sort_list[1])
	to_sort_list.append(output)
	return sort_with_efficient_memory(to_sort_list[2:])

sort_with_efficient_memory([[4],[1],[2],[0]])

# This traverses the complete list always. This is not needed
# Reasoning: If Already one is sorted then it's that you need 
# to find the position for the second
def sorted_two_arrays(array1, array2):
	i=0
	j=0
	result = []
	while(i<len(array1) and j<len(array2)):
		if array1[i] < array2[j]:
			result.append(array1[i])
			i +=1
		else:
			result.append(array2[j])
			j +=1
	if (i<len(array1)):
		result.extend(array1[i:])
	if (j<len(array2)):
		result.extend(array2[j:])
	return result

sorted_two_arrays([],[1,2])



# Input: list_of_files that contain the calculated o/p
def external_sort(list_of_files):
	# Read through the directory 
	# form the structure
	get_min_input = map(form_get_min_input, list_of_files)
	while(len(get_min_input) > 0):
		min_value, min_index = get_min(get_min_input)
		print(min_value)
		if len(get_min_input[min_index][0]) == 0:
			get_min_input = get_min_input[0:min_index] + get_min_input[min_index+1:]

external_sort(['/var/tmp/1_1','/var/tmp/2_1'])

def sort_file(file_name):
	with open(file_name,'r') as fp:
		output = map(lambda x: x + '\n', map(str,sorted(map(int,fp.readlines()))))
	with open(file_name+"_1",'w') as out_fp:
		out_fp.writelines(output)


sort_file('/var/tmp/2')

def form_get_min_input(file_name):
	fp = open(file_name,'r')
	return [read_from_file(fp,3),fp]


# This method takes input as the following structure
# [([],fp)] - List of Tuples, Each tuple contains a 
# list (containing some elements from the file) and a fp 
# Return: The min value after removing it from input_struct
def get_min(input_struct):
	cur_min = input_struct[0][0][0]
	cur_min_index = 0
	i = 1
	while(i<len(input_struct)):
		curr_input = input_struct[i]
		if curr_input[0][0] < cur_min:
			cur_min = curr_input[0][0]
			cur_min_index = i
		i += 1
	input_struct[cur_min_index][0] = input_struct[cur_min_index][0][1:]
	if len(input_struct[cur_min_index][0]) == 0:
		result = read_from_file(input_struct[cur_min_index][1],3)
		# Not a good idea to modify the input here, so better modify at the caller
		input_struct[cur_min_index][0]  = result
	return (cur_min, cur_min_index)

get_min_input = [
	[[1,2,3],open("/var/tmp/1","r")],
	[[10,20,30],open("/var/tmp/2","r")]
]
get_min(get_min_input)

def read_from_file(file_pointer, line_count):
	i = 0
	result = []
	while(i<line_count):
		result.append(file_pointer.readline().strip())
		i += 1;
	result = remove_empty_lines(result)
	result = map(int,result)
	return result

def remove_empty_lines(input):
	output = []
	for i in input:
		if (len(i) > 0):
			output.append(i)
	return output

file_pointer = open("/var/tmp/1","r")
print(read_from_file(file_pointer,10))
print(read_from_file(file_pointer,10))

def sorted_square(curr_input):
	partition = binary_search(curr_input)
	i = partition
	j = partition - 1
	result = []
	while(i<len(curr_input) and j>=0):
		if(abs(curr_input[i])<abs(curr_input[j])):
			result.append(curr_input[i] * curr_input[i])
			i+=1
		else:
			result.append(curr_input[j] * curr_input[j])
			j-=1
	while(i<len(curr_input)):
		result.append(curr_input[i] * curr_input[i])
		i+=1
	while(j>=0):
		result.append(curr_input[j] * curr_input[j])
		j-=1
	print(result)

curr_input = [-9,-1]
sorted_square(curr_input)

def binary_search(curr_input):
	start = 0
	end = len(curr_input) - 1
	while(start<=end):
		mid = start + (end-start)/2
		if(curr_input[mid] >= 0 and mid-1 >= 0 and curr_input[mid-1] < 0):
			return mid
		if curr_input[mid] > 0:
			end = mid - 1
		else:
			start = mid + 1
	return 0

binary_search_input = [7,8,1,2,3,6]
binary_search(binary_search_input)


def read_file():
	with open('/var/tmp/j','r') as f:
		for l in f:
			print(l)

