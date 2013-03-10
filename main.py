import texIO
import table
import conversion


def main():
	data = texIO.getEnglishFile("J:\Creation\Computer_Science\Projects\Text_to_TeX","test.txt")
	data = conversion.convertData(data)
	texIO.writeToTexFile(data,"testTex.tex")

main()