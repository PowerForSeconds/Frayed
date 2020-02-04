import sys
file = open(sys.argv[1], "r")
lines = file.read().split(";")

for line in range(len(lines)):
    lines[line] = lines[line].split(" ")
    for n in range(len(lines[line])):
        if "\n" in lines[line][n]:
            lines[line][n] = lines[line][n].replace("\n", "")
print(lines)

storage = {}

useless = None

for n in range(len(lines)):
    line = lines[n]
    if line[0] in ["var", "variable"] and len(line) in [3]:
        try:
            line[1] = int(line[1])
            ## ERROR
        except:
            try:
                line[2] = int(line[2])
                storage[line[1]] = line[2]
            except:
                try:
                    storage[line[1]] = storage[line[2]]
                except:
                    pass
                    ## ERROR

print(storage)
input()
