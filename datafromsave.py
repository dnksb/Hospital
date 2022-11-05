data = []
file_name = str(R'Save/SaveLV.txt')

with open(file_name) as file:
	line = file.readlines()
	
	for x in line:
		if(x == 'False'):
			data.append(0)
		else:
			data.append(int(x))

level = data[0]
