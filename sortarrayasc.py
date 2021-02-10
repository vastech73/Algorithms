import time
start_time = time.time()
l1 = [ 3, 5, 2, 4,7,9,12,14,15,6]
temp = 0

for i in range(0,len(l1)):
    # Sort from the beginning. 
    # Check whether the first number is greater than the next number
    # if it is then move it to the next position
    for j in range(i+1,len(l1)):
        if (l1[i] > l1[j]):
            temp = l1[i]
            l1[i] = l1[j]
            l1[j] = temp
print(l1)

print("--- %s seconds ---" % (time.time() - start_time))
