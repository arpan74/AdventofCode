floor = 0
counter = 1
for i in (open("input.txt")).read():
	if i == "(":
		floor = floor + 1
	if i == ")":
		floor = floor - 1
	if floor == -1:
		print counter
		break
	counter = counter + 1
