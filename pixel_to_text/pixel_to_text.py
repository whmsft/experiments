from math import sqrt

# Split characters into a list of them and sqrt of length
def splitize(chars):
	# Retrieve Characters from the list
	split_list = [char for char in chars]
	# Have the sqrt of the length
	square_root_length = sqrt(len(split_list))
	# Return the two value as a tuple
	return split_list, square_root_length

def match_value(v1, v2):
	# Find out all intersecting characters
	common_characters = [char for char in v1[0] if char in v2[0]]
	# Return as a value
	return len(common_characters)/v1[1]/v2[1]

# A B C D
# E F G H
# I J K L
# M N O P

D1 = [
	[0, 0, 1, 1, 0, 0, 0, 0],
	[0, 0, 1, 1, 0, 0, 0, 0],
	[0, 0, 1, 1, 0, 0, 0, 0],
	[1, 1, 1, 1, 1, 1, 1, 1],
	[1, 1, 1, 1, 1, 1, 1, 1],
	[0, 0, 1, 1, 0, 0, 0, 0],
	[0, 0, 1, 1, 0, 0, 0, 0],
	[0, 0, 1, 1, 0, 0, 0, 0]
]

def match(D1, D2):
	matche = 0
	scaned = 0
	for y in range(len(D1)):
		for x in range(len(D1)):
			scaned += 1
			if D1[y][x] == D2[y][x]:
				matche += 1
	return (matche/scaned)*100