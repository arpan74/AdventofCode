usrinput = open("input.txt").read()

x = {}


xCor = 0
yCor = 0
for i in usrinput:
	
	if( i == "^"):
		yCor = yCor + 1
	if( i == "v"):
		yCor = yCor - 1
	if( i == ">"):
		xCor = xCor + 1
	if( i == "<"):
		xCor = xCor - 1
		
	if( xCor in x):
		if( yCor in x[xCor]):
			x[xCor][yCor] = x[xCor][yCor] + 1
		x[xCor] = {yCor:1}
	if( xCor not in x):
		x[xCor] = {yCor:1}

print x