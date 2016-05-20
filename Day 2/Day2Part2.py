def DetermineRib(l, w, h):
	surfA = l*w*h
	if min((l*w),(w*h),(l*h)) == l*w:
		return (l + l + w + w) + surfA 
	if min((l*w),(w*h),(l*h)) == w*h :
		return (w + w + h + h) + surfA
	return (l + l + h + h ) + surfA
sum = 0

for line in open("input.txt"):
	strA = line.split("x")
	sum = sum + DetermineRib(int(strA[0]), int(strA[1]), int(strA[2]))
print sum

