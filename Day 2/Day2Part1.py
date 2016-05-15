def surfaceArea(l, w, h):
	return 2*(l * w) + 2*(w * h) + 2*(l * h) + min((l*w),(w*h),(l*h))
sum = 0

for line in open("input.txt"):
	strA = line.split("x")
	sum = sum + surfaceArea(int(strA[0]), int(strA[1]), int(strA[2]))
print sum

