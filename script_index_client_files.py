import os
from tkinter import Tk, filedialog
from datetime import datetime


# asks the user to select the directory
open_file = filedialog.askdirectory()


# extract a list of all the files and directories contained in the directory selected by the user
list_pathnames =[]
for root, dirs, files in os.walk(open_file, topdown=False):
	for name in files:
#		print(os.path.join(root, name))
		list_pathnames.append(os.path.join(root, name))
	for name in dirs:
#		print(os.path.join(root, name))
		list_pathnames.append(os.path.join(root, name)) 

# re-order the list of paths by alphabetical order - os.walk does not work alphabetically by default
sorted_list = sorted(list_pathnames)

# transform the pathname into a list of the subfolders and files
list_splitted_pathnames_sorted = []
for element in range(len(sorted_list)):
	list_splitted_pathnames_sorted.append(sorted_list[element].split("/"))


list_to_print = []
for n in range(len(list_splitted_pathnames_sorted)):
#	print( len(list_splitted_pathnames_sorted[n])*"---" + list_splitted_pathnames_sorted[n][-1])
	list_to_print.append((len(list_splitted_pathnames_sorted[n])-7)*"---" + list_splitted_pathnames_sorted[n][-1])


# prints the indented file and directory names into a text file with the current year and month
# this index file is automatically created into the directory selected by the user initially

filename = "file_index_" + datetime.now().strftime("%Y_%m")
lines = list_to_print
with open(open_file + "//" + filename + '.txt', 'w') as f:
    f.write('\n'.join(lines))