maximum = 20
count = maximum

found = False

while(not found):
	for x in range(1,maximum+1):
		if(count % x != 0):
			break
		if(x == maximum):
			found = True
	
	if(not found):
		count += maximum

print(count)
	
