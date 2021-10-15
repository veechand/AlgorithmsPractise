def is_bst(preorder):
	stack = []
	cur_root_value = -2**32
	for i in preorder:
		if i < cur_root_value:
			return False
		if (len(stack) > 0 and stack[-1] < i):
			cur_root_value = stack.pop()
		stack.append(i)
	return True

pre1 = [40 , 30 , 35 , 80 , 100]
pre1 = [40 , 30 , 35 , 20 ,  80 , 100]
print(is_bst(pre1))