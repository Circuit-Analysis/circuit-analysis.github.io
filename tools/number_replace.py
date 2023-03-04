
# Read in the file
with open('chapter-13.md', 'r') as file :
  filedata = file.read()

# Replace the target string
counter = 0
while 'LABEL_FOR_THIS_IMAGE' in filedata:
  filedata = filedata.replace('LABEL_FOR_THIS_IMAGE', 'LABEL_'+str(counter), 1)
  counter = counter + 1
  print(counter)

# Write the file out again
with open('file.txt', 'w') as file:
  file.write(filedata)

