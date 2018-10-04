'''
#file_path=open("new_text.txt")
file_path=open("new_text.txt","r")  # read only

print(file_path.read())
file_path.close()
'''

'''
#file_path=open("new_file.txt","w")  # write only
file_path=open("new_file.txt","a")  # for append only
# if we run this file again it will overwrite the file
file_path.write("God is great")
#file_path.write("This is new added line")
file_path.close()
'''

file_path=open("append_ex.py","a+")
#file_path.write("First operation")
file_path.write(" Third operation")
file_path.seek(11) #cursor start reading from that point
print(file_path.read())
file_path.close()

#buffering is dependent on client server application
#buffering size in kb
#if its defined  as 0 so no buffering heppen but 1 or morethan 1 value depend on overall system
#serever+network connectivity +client application=======etc are some components for buffering