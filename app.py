import os
import filecmp
import sys

if len(sys.argv) == 1:
    print( "Give input directory as an argument")
    exit(1)

inp = sys.argv[1] # directory
files = os.listdir(inp)

outs = [[files[0]]]
for i in range(1, len(files)):
    fl = 0
    for ls in outs:
        if filecmp.cmp(files[i], ls[0]):
            ls.append(files[i])
            fl = 1
            break
    if fl == 0:
        outs.append([files[i]])

for ls in outs:
    if len(ls)>1:
        print(ls)
        