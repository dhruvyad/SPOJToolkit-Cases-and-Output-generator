from sys import argv
import subprocess
import os

def main():
	solutionfile = argv[1]
	problemid = argv[2]
	os.popen('python scripts/getcases.py %s' % problemid)
	os.popen('python scripts/getoutput.py %s %s' % (solutionfile, problemid))
	os.popen('python scripts/correct.py %s %s' % (solutionfile, problemid))

main()
 
