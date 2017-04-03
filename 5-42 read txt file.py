def printFileContent(fileName):
	f = open(fileName, 'r')
	content = f.readlines()
	#print [i.rstrip("\n") for i in content]
	for line in content:
		print line.rstrip("\n")
	f.close()

def addTextToFile(fileName, text):
	f = open(fileName, 'a')
	f.write(text)
	f.close()

def writeFile(fileName, text):
	f = open(fileName, 'w')
	f.write(text)
	f.close()


def main():
	writeFile("test.txt", "1 linea\n")
	addTextToFile("test.txt", "2 linea")
	printFileContent("test.txt")

main()
