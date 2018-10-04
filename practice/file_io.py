file_path = open('test.txt','w+') 
file_path.write('test')
file_path.close()

file_path = open('test.txt','a+')
file_path.write('test1')
#file_path = open('test.txt','r')
file_path.seek(1)
print(file_path.read())
file_path.close()

