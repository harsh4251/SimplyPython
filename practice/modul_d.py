'''
import os
value=os.getcwd()
print(value)

list_val=os.listdir(value)'''
'''print(list_val)

for data_q in list_val:
	print(value + "\\" + data_q)
'''

#os.mkdir(value +"\\" + "New_testing_folder")	
#os.remove(value +"\\" + "demo.txt")
#os.rmdir(value+ "\\" + "New_testing_folder")

#os.rename(value + "\\" + "temp",value + "\\" + "temp_new")#

'''
for help
import os
help os'''

import sys

'''print (len(sys.argv))
print (sys.argv)
val_p=sys.copyright

print(val_p)
print(sys.maxsize) #  maximum size of datatype change according to bitwise os
print(sys.path)'''
'''
'''
'''
def funct(x):
	if x>10:
		return x
	else:
		print (x)
		x=funct(x+1)
		
		return x
print("funct gets back{0}".format(funct(0)))
'''
'''
print(sys.getrecursionlimit())
#print(sys.setrecursionlimit(limit))
'''

import time
'''
print(time.clock())
print(time.ctime()) # showing time in string
print(time.time())
new_time=time.time()-86400 #86400 is i day time in seconds

print(time.ctime(new_time))
'''
'''
while True :
	print(time.ctime())
	time.sleep(2)
	
'''
'''
import tobomported

print(tobomported.multiply(1,2))
print(tobomported.multiply(1,2))
print(tobomported.value)

'''

#for modules store in different diractory
#E:\Python\Learn_py2\Start\demo_temp
import sys
sys.path.append("E:\\Python\\Learn_py2\\Start\\demo_temp")

#print(sys.path)

#import str_opration as str_M
#print(str_M.str_reverse("Good Day"))

#for import the specific funtion or method from a modules
#from str_opration import str_reverse,addition 

#__init__.py is required to check if the directory is py directory or not
#xyz is package or directory name where all the python files are exist
#and we want to use one from there
#__init__.py should be exist in xyz as a blank file or contain some comman methods
#otherwise module does not exist kind of error will occur.

from xyz.str_opration import str_reverse,addition 

print(str_reverse("Good Day"))
print(addition(4,7))


#
