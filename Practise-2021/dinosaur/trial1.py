from math import sqrt

dataset1 = open("/var/tmp/dataset1.txt","r")
dataset2 = open("/var/tmp/dataset2.txt","r")

dataset2_details = {}
not_sorted_output = []

for line in dataset2:
	name,stride_length,stance = map(lambda x:x.strip(), line.split(",")) #check if it always contains 3
	if (stance == "bipedal"):
		dataset2_details[name] = stride_length
print(dataset2_details)	

for line in dataset1:
	name,leg_length,diet = map(lambda x:x.strip(), line.split(","))
	if name in dataset2_details:
		speed = ((float(stride_length) / float(leg_length) - 1) * sqrt(float(leg_length) * 9.8))
		not_sorted_output += [(name,speed)]

print(not_sorted_output)
output = sorted(not_sorted_output,key=lambda x: x[1])

print(output)