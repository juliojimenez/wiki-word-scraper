from optparse import OptionParser
import requests
import re
import os
from shutil import copyfile

def scraper(filename):
	while True:
		try:
			randomWiki = requests.get("https://www.wikipedia.org/wiki/Special:Random")
			print "[w] Scraping %s" % randomWiki.url

			regex = re.findall(r'[a-zA-Z]+', randomWiki.text)
			lowerList = [x.lower() for x in regex]
			print "[w] Total Words: %d" % len(lowerList)
			uniqueList = list(set(lowerList))
			print "[w] Unique Words: %d" % len(uniqueList)

			with open(filename, 'a') as f:
				for x in uniqueList:
					f.write(x + "\n")
	
			with open(filename, 'r') as fileCleanup:
				dirty = []
				for x in fileCleanup:
					dirty.append(x[:-1])
				clean = list(set(dirty))
				clean.sort()
				print "\n[f] Total words in file: %d" % len(clean)
			
			copyfile(filename, filename + ".bak")
			os.unlink(filename)
			 
			with open(filename, 'a') as fileWrite:
				for x in clean:
					fileWrite.write(x + "\n")

			fileSize = float(os.path.getsize(filename)) / 1000000
			print "[f] File Size: %.2f MB\n" % fileSize
			
			os.unlink(filename + ".bak")
		except KeyboardInterrupt:
			print " Thanks for playing!"
			break
	return True

def main():
	print ""
	print " Wiki Word Scraper v0.0.3"
	print " Julio Jimenez"
	print ""

	usage = "Usage: %prog [options] arg"
	parser = OptionParser(usage)
	parser.add_option("-o", "--output", action="store", type="string", dest="output", help="Output wordlist file.")

	(options, args) = parser.parse_args()

	if options.output != None:
		scraper(options.output)
	else:
		parser.print_help()

	return True	

if __name__ == "__main__":
	main()	