

ones = "one two three four five six seven eight nine".split(" ")

teens = "ten eleven twelve thirteen fourteen fifteen sixteen seventeen eighteen nineteen".split(" ")

tens = "ten twentyrty fifty sixty seventy eighty ninety".split(" ")

hundred = "hundred"

word_and = "and"


ans = 0


#add 1 - 9
for i, item in enumerate(ones):
	ans += len(item)
	#print(item)


# add 10 - 19
for i, item in enumerate(teens):
	ans += len(item)
	#print(len(item))


# add 20 - 99
for i in range(1, len(tens)):

	ans += len(tens[i])
	for digit in ones:
		ans += len(tens[i]) + len(digit)


for digit in ones:
	# add x00
	ans += len(digit)
	ans += len(hundred)
	#print(digit+hundred)

	# add x01 - x09
	for item in ones:
		ans += len(digit)		
		ans += len(hundred)
		ans += len(word_and)
		ans += len(item)
	#	print(digit+hundred+word_and+item)
	# add x10 - x19

	for item in teens:
		ans += len(digit)
		ans += len(hundred)
		ans += len(word_and)
		ans += len(item)
	#	print(digit+hundred+word_and+item)

	# add x20 - x99
	for i in range(1, len(tens)):

		ans += len(digit)
		ans += len(hundred)
		ans += len(word_and)		
		ans += len(tens[i])
		#print(digit+hundred+word_and+tens[i])
		for digits in ones:
			ans += len(digit)
			ans += len(hundred)
			ans += len(word_and)
			ans += len(tens[i]) + len(digits)
		#	print(digit+hundred+word_and+tens[i]+digits)

ans += len("one")
ans += len("thousand")

print(ans)



