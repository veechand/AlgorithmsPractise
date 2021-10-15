 
a = [4,3,2,1]
start = 0
end = len(a) - 1
f_s = a[start]
e_s = a[end]
found = False
while (start<end):
	if(f_s == e_s and start == end - 1):
		found = True
		break
	elif (f_s < e_s):
		start += 1
		f_s += a[start]
	else:
		end -= 1
		e_s += a[end]
if (found):
	print(start,end)
else:
	print("Not found")


		

