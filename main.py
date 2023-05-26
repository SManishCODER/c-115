import os
  
  
# Source file path
source = 'man.txt'
  
# destination file path
dest = 'file.txt'
  

os.rename(source, dest)
print("Source path renamed to destination path successfully.")