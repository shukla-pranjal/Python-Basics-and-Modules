#file_object = open("file_adress" , 'mode')
file = open("virtual.txt")
print(file)#<_io.TextIOWrapper name='virtual.txt' mode='r' encoding='cp1252'>
text = file.read()
print(text)
"""r (default mode) read mode gives error when file not exist 
w write mode not gives if file exist overwrite else it creates new
a append mod
rt read in text mode (default)
rb read in binary mode
"""
file.close()

"""with open("file_address" , 'mode') as f: by this mthod not needed to close    #...

 fileobject.readline() -> return one line of file and move cursror at starting of next line
 its type is stirng
 
 write lines accept in list
 
 seek and tell in python works in file objects
 
 truncate ->  fileobject.truncate(x)
 x is only integer
 truncate only show starting character x 
 like
 f.write("hello world")
 f.truncate(3) #this only write 3 character in file 
 # only hel will write in file
 
 
 """







"""
─── seek & tell ──────────────────────────────────────────────────────────────

fileobject.tell()  -> returns the current byte position of the file pointer.

fileobject.seek(offset, whence=0)
    offset  : number of bytes to move
    whence  : 0 = from start (default), 1 = from current position, 2 = from end

IMPORTANT – .read() moves the pointer to the END of the file.
  A second call to .read() will return an empty string because the pointer
  is already at the end.  Use .seek(0) to reset before reading again.

Example:
    with open("virtual.txt", "r") as f:
        data = f.read()        # reads all content; pointer now at end
        print(f.tell())        # prints file size in bytes

        f.seek(0)              # reset pointer to beginning
        data_again = f.read()  # works correctly now
"""

