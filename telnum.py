import random
ccode = '+91'
gen_random_first = '9'
file1 = open('telnum.csv','w')
for i in range(0,1000):
    gen_random_second = ''.join(["{}".format(random.randint(0, 9)) for num in range(0, 9)])
    tel_num = ccode+'-'+ str(gen_random_first)+str(gen_random_second)
    file1.write(tel_num)
    file1.write('\n')
    if i == 500:
        ccode = '+92'
        gen_random_first = '4'
    print(tel_num)
file1.close()
