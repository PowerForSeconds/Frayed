import sys

def error(cause):
    print()
    print(cause)
    print()
    input("Press RETURN to exit the program")

file = open(sys.argv[1], "r")
lines = file.read().split(";")

for line in range(len(lines)):
    lines[line] = lines[line].split(" ")
    for n in range(len(lines[line])):
        if "\n" in lines[line][n]:
            lines[line][n] = lines[line][n].replace("\n", "")

storage = {}

useless = None
exiting = False

for n in range(len(lines)):
    if exiting:
        break
    line = lines[n]
    if line[0] == "var":
        if len(line) == 3:
            try:
                line[1] = int(line[1])
                error("Variable name cannot be a number" + "\n" + "Line " + str(n + 1))
                exiting = True
                
            except:
                try:
                    line[2] = int(line[2])
                    storage[line[1]] = line[2]
                except:
                    try:
                        storage[line[1]] = storage[line[2]]
                    except:
                        error("Variable " + str(line[2]) + " does not exist" + "\n" + "Line " + str(n + 1))
                        exiting = True
        else:
            error("Var takes 2 inputs, not " + str(len(line) - 1) + "\n" + "Line " + str(n + 1))
            exiting = True

    if line[0] == "add":
        if len(line) == 3:
            total = 0
            try:
                line[1] = int(line[1])
                total += line[1]
            except:
                try:
                    total += storage[line[1]]
                except:
                    error("Variable " + str(line[1]) + " does not exist" + "\n" + "Line " + str(n + 1))
                    exiting = True
            try:
                useless = storage[line[2]]
                storage[line[2]] += total
            except:
                error("Variable " + str(line[2]) + " does not exist" + "\n" + "Line " + str(n + 1))
                exiting = True
        else:
            error("Add takes 2 inputs, not " + str(len(line) - 1) + "\n" + "Line " + str(n + 1))
            exiting = True

    if line[0] == "sub":
        if len(line) == 3:
            total = 0
            try:
                line[1] = int(line[1])
                total += line[1]
            except:
                try:
                    total += storage[line[1]]
                except:
                    error("Variable " + str(line[1]) + " does not exist" + "\n" + "Line " + str(n + 1))
                    exiting = True
            try:
                useless = storage[line[2]]
                storage[line[2]] -= total
            except:
                error("Variable " + str(line[2]) + " does not exist" + "\n" + "Line " + str(n + 1))
                exiting = True
        else:
            error("Add takes 2 inputs, not " + str(len(line) - 1) + "\n" + "Line " + str(n + 1))
            exiting = True

print(storage)
input()
