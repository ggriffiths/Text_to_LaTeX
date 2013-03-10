import re
import table

# Replace last n occurrences of 'old' in string 's' with 'new'.
def replaceLast(s,old,new,n):
	x = s.rsplit(old, n)
	return new.join(x)

# Converts data set of English lines into LaTeX
def convertData(data):
	for index in range(len(data)):
		# Find section that needs converting
		sectionObj = re.search("\$.+\$",data[index])
		
		# Convert single line
		if sectionObj:
			data[index]=data[index].replace(sectionObj.group(),convertTunnel(sectionObj.group()))

		# Fix bracket formatting
		data[index]=data[index].replace(";@BO","{")
		data[index]=data[index].replace(";@BC","}")
	return data

# Converts a single section inside $...$
def convertTunnel(section):
	section=section.replace(section,convertSection_patternSwap(section))
	section=section.replace(section,convertSection_simpleSwap(section))
	return section

# Converts complex english expression into LaTeX
def convertSection_patternSwap(section):
	# Search for an inner section. If found, convert it
	innerSearchObj = re.search("\{.+\}",section)

	if innerSearchObj:
		# Get Inner Temp String to operate on
		tempInnerStr = innerSearchObj.group()

		# Replace your tempStr with ;@INNER to operate on
		section = section.replace(tempInnerStr,";@INNER")

		# Change First & Last Brackets of the temp string
		tempInnerStr = tempInnerStr.replace("{",";@BO",1)
		tempInnerStr = replaceLast(tempInnerStr,"}",";@BC",1)

		# Converts given section with ;@INNER tag
		section = section.replace(section,patternSwap(section))

		# Converts ;@INNER tag
		section = section.replace(";@INNER",convertSection_patternSwap(tempInnerStr))

	return patternSwap(section)

# Converts a section of complex sentences into LaTeX
def patternSwap(section):
	for pattern in table.patternSwapTable:
		searchObj = re.search(pattern[0],section,re.IGNORECASE)
		if searchObj:
			section = (section.replace(searchObj.group(),pattern[1](section)))
	return section

# Converts simple symbols into LaTeX equivalent
def convertSection_simpleSwap(section):
	for pattern in table.swapTable:
		if pattern[0] in section:
			section = section.replace(pattern[0],pattern[1])
	return section
	
# Specific Conversion Methods
def toIntegral(section):
	section = section.strip("\$|;@BO|;@BC").split()
	return "\int\limits_{" +section[4]+ "}^{"+section[6]+"}"+section[2]

def toDoubleIntegral(section):
	section = section.strip("\$\{\}|;@BO|;@BC").split()
	return "\int\limits_{"+section[5]+ "}^{"+section[7]+"}"+"\int\limits_{"+section[9]+ "}^{"+section[11]+"}"+section[3]

def toTripleIntegral(section):
	section = section.strip("\$\{\}|;@BO|;@BC").split()
	return "\int\limits_{"+section[5]+ "}^{"+section[7]+"}"+"\int\limits_{"+section[9]+ "}^{"+section[11]+"}"+"\int\limits_{"+section[13]+ "}^{"+section[15]+"}"+section[3]
	
def toSummation(section):
	section = section.strip("\$\{\}|;@BO|;@BC").split()
	return "\sum\limits_{" +section[4]+ "}^{"+section[6]+"}"+section[2]