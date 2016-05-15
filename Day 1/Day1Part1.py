floor = 0

for i in (open("input.txt")).read():
	if i == "(":
		floor = floor + 1
	if i == ")":
		floor = floor - 1
print floor
