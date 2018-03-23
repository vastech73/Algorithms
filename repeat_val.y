'''
Python program to get the first occurence of a repeating element in an array
'''

def repeat_val(lst):
	for i in range(len(lst)):
		if i in lst[i:]:
			print('First Occurence:{}'.format(i))
	return lst[i]

lst = [4, 9, 1, 1]
print(repeat_val(lst))
