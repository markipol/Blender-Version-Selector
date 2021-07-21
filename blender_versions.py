import os, sys

path = os.path.dirname(os.path.realpath(__file__))
print(path)
default = "2.93.1"

directory_contents = os.listdir(path)
print(directory_contents)
for item in directory_contents:
	if os.path.isdir(item):
		print(item)
		
versioninput = input("Please select one of the above versions, or press enter for the default, which is " + default + "\n")
if  not versioninput:
	finalversion = default
elif versioninput in directory_contents:
	
	finalversion = versioninput
else:
	print("Error, please select a version from above")
	quit()
#print(finalversion)
if len(sys.argv) == 1:
	cmd = ".\\" + str(finalversion) + "\\blender.exe"
elif len(sys.argv) == 2 and os.path.exists(sys.argv[1]):
	cmd = ".\\" + str(finalversion) + '\\blender.exe "' + sys.argv[1] + '"'
else:
	print("Error, either too many arguments (only one allowed, the blend file to open) or file path doesn't exist")
print(cmd)
os.system(cmd)