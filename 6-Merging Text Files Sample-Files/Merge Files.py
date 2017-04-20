import glob2

def getFileList(fileNameFilter=""):
	return glob2.glob(fileNameFilter)


def main():
	fileNames = getFileList("*.txt")
	with open("merge.txt","w") as newFile:
		for fileName in fileNames:
			with open(fileName,"r") as fileToMerge:
				print "Writing: " + fileName
				newFile.write(fileToMerge.read() + "\n")
			

main()
