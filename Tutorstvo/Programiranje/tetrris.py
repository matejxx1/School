c, p = [int(x) for x in input().split()]
stolpec = [int(x) for x in input().split()]

def figura1(vsota):
	for i in range(c - 3):
		if stolpec[i] == stolpec[i+1] == stolpec[i+2] == stolpec[i+3]:
			vsota += 1
	return vsota

def figura2(vsota):
	for i in range(c - 1):
		if stolpec[i] == stolpec[i+1]:
			vsota += 1
	return vsota

def figura3(vsota):
	for i in range(c - 2):
		if stolpec[i] == stolpec[i+1] == stolpec[i+2] - 1:
			vsota += 1
	for i in range(c - 1):
		if stolpec[i] - 1 == stolpec[i+1]:
			vsota += 1
	return vsota

def figura4(vsota):
	for i in range(c - 2):
		if stolpec[i] - 1 == stolpec[i+1] == stolpec[i+2]:
			vsota += 1
	for i in range(c - 1):
		if stolpec[i] == stolpec[i+1] - 1:
			vsota += 1
	return vsota

def figura5(vsota):
	for i in range(c - 2):
		if stolpec[i] == stolpec[i+1] == stolpec[i+2]:
			vsota += 1
		if stolpec[i] - 1 == stolpec[i+1] == stolpec[i+2] - 1:
			vsota += 1
	for i in range(c - 1):
		if stolpec[i] == stolpec[i+1] - 1:
			vsota += 1
		if stolpec[i] - 1 == stolpec[i+1]:
			vsota += 1
	return vsota

def figura6(vsota):
	for i in range(c - 2):
		if stolpec[i] == stolpec[i+1] == stolpec[i+2]:
			vsota += 1
		if stolpec[i] == stolpec[i+1] - 1 == stolpec[i+2] - 1:
			vsota += 1
	for i in range(c - 1):
		if stolpec[i] == stolpec[i+1]:
			vsota += 1
		if stolpec[i] - 2 == stolpec[i+1]:
			vsota += 1
	return vsota

def figura7(vsota):
	for i in range(c - 2):
		if stolpec[i] == stolpec[i+1] == stolpec[i+2]:
			vsota += 1
		if stolpec[i] - 1 == stolpec[i+1] - 1 == stolpec[i+2]:
			vsota += 1
	for i in range(c - 1):
		if stolpec[i] == stolpec[i+1]:
			vsota += 1
		if stolpec[i] == stolpec[i+1] - 2:
			vsota += 1
	return vsota

if p == 1:
	print(figura1(c))
elif p == 2:
	print(figura2(0))
elif p == 3:
	print(figura3(0))
elif p == 4:
	print(figura4(0))
elif p == 5:
	print(figura5(0))
elif p == 6:
	print(figura6(0))
else:
	print(figura7(0))
