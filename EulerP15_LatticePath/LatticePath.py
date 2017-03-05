# def traverse(start, end):

# 	open_list = []

# 	move = [(1,0), (0,1)]

# 	if start == end:
# 		return 0

# 	open_list.append(start)
	
# 	n_route = 0
# 	memo = {}
# 	while(open_list):

# 		current = open_list.pop()

# 		#generate nodes
# 		for i, item in enumerate(move):

# 			temp = (current[0] + item[0], current[1] + item[1])

			
# 			if temp[0] in range(0, end[0]+1) and temp[1] in range(0,end[1]+1):
# 				successor = temp

# 				if successor == end:
# 					n_route += 1	
				

# 				open_list.append(successor)


# 	return n_route

def minus(x,y):
	return x-y

def find_nroute(memo,start,end):
	move = [(1,0), (0,1)]
	
	#print(end)
	if end in move:
		return 1

	if end in memo:
		nroute = memo[end]
	else:
		
		temp_1 = tuple(map(minus, end,move[0]))
		temp_2 = tuple(map(minus, end,move[1]))

		range_x = range(0, end[0] + 1)
		range_y = range(0, end[1] + 1)

		cond_1 = temp_1[0] in range_x and temp_1[1] in range_y
		cond_2 = temp_2[0] in range_x and temp_2[1] in range_y

		if cond_1 and cond_2:
			nroute = find_nroute(memo,start, temp_1) + find_nroute(memo,start, temp_2)
		elif (cond_1 and not cond_2):
			nroute = find_nroute(memo,start, temp_1)
		elif (cond_2 and not cond_1):
			nroute = find_nroute(memo,start, temp_2)


	memo[end] = nroute
	return nroute


memo = {}
start = (0,0)
end = (20,20)
print(find_nroute(memo, start, end))

#print(memo)