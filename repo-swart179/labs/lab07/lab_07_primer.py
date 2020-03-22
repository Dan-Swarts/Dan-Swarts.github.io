import random

file_name = input('enter the file name: ')



int(round((random.random()-0.5)*2000))

file_obj = open('file_name',w)
for i in range(0,1000):
    record = ''
    record += i + str(int(round((random.random()-0.5)*2000)))
    file_obj.write(record)
    if i != 1000:
        file_obj.write(\n)
file_obj.close()