# -problem3_6.py *- coding: utf-8 -*-

import sys

filename1 = sys.argv[1]
filename2 = sys.argv[2]

text_file = open(filename1)
save_file = open(filename2, 'w')

for line in text_file:
    line = line.replace("\n","")
    save_file.write(str(len(line)))
    save_file.write("\n")
    
text_file.close()
save_file.close()
