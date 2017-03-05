def GetNextCollatz(n):
	if int(n) & 1 : #if odd
		return 3*n+1
	else: #if even
		return n/2


if __name__ == "__main__":

	i = 2
	ans = 0
	maxcount = 0

	memo = {}
	while i < 1000000:
		#print(i)
		n = i
		count = 0
		while True:
			
			if n in memo:
				count = memo[n] + count
				break
			else:
				count += 1
			
			n = GetNextCollatz(n)

			if n == 1:
				count += 1
				break

		if count > maxcount:
			maxcount = count
			ans = i

		memo[i] = count
		i += 1

	print(ans)	


## 2s solution  
# def collatz_len(C, n):
#     if n in C:
#         return C[n]
#     else:
#         if n % 2 == 0:
#             C[n] = collatz_len(C,n//2)+1
#         else:
#             C[n] = collatz_len(C,3*n+1)+1
#     return C[n]

# C = {1:1}
# max_n = 1
# max_len = 1
# for n in range(2,1000000+1):
#     next_len = collatz_len(C,n)
#     if next_len > max_len:
#         max_n = n
#         max_len = next_len
# print(max_n, max_len)