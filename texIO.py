import os

# Read the .txt file of english commands and put into a list
def getEnglishFile(location,file):
	os.chdir(location)        
	with open(file, 'r') as textFile:									
		textLines = [line.strip() for line in textFile]
	return textLines

# Write the new list of commands into a .tex file
def writeToTexFile(texCommands,title):
	texFile = file(title,"w+")
	texFile.write("\\begin{document}")
	for command in texCommands:
		texFile.write("%s\n" % command)
	texFile.write("\end{document}")
