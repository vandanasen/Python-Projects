
#writing to a file
text="sample text to save a file "
saveFile=open('exampleFile.txt','w')
saveFile.write(text)
saveFile.close()
#appending a file
appendMe='\n new bit of info that i wanted to add to the file that is there'
appendFile=open('exampleFile.txt','a')
appendFile.write(appendMe)
appendFile.close()
#reading a file
readMe=open('exampleFile.txt','r').read()
print(readMe)
#reading a file line by line
readMe=open('exampleFile.txt','r').readlines()
print(readMe)

