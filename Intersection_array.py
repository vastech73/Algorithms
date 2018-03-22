import time
'''
Python program to get the intersection of two arrays
'''

def intersect_array(lst1, lst2):
	start_time = time.time()
	union_arr = []
	for i in lst1:
		for j in lst2:
			if i == j:
				if i not in union_arr:
					union_arr.append(i)
	print(time.time() - start_time)

	return union_arr

lst1 = [ 4, 9, 1, 17, 11, 26, 28, 28, 26, 66, 91]
lst2 = [9, 9, 74, 21, 45, 11, 63]
print(intersect_array(lst1,lst2))
