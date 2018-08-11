import sys
import os
import os.path

mypath = os.path.dirname(os.path.realpath(__file__))
files = [f for f in os.listdir(mypath) if f.endswith(".ui")]

for i,x in zip(files, range(1,len(files)+1)):
	print("Converting {} to {}.py".format(i, i.split(".")[0]))
	os.system("pyside2-uic {} -o {}.py".format(i, i.split(".")[0]))
	print("Done ({}/{})".format(x,len(files)))
print("Finished!")