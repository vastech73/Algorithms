'''
Python program to remove duplicates number from a list
Create a new list which has the duplicates skipped
'''

def remove_duplicates(lst):
	dup_val_lst = []
	for i in lst:
		if i not in dup_val_lst:
			dup_val_lst.append(i)
	return dup_val_lst




lst = [45,45,100,78,78,34,34,2,1,230,230]
print(remove_duplicates(lst))
