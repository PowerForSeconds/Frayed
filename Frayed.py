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

n = 0

while n < len(lines):
    if exiting:
        break
    line = lines[n]
    if line[0] == "//":
        pass
    if line[0] == "RETURN":
        if len(line) == 2:
            try:
                line[1] = int(line[1])
                print(line[1])
                
            except:
                print(storage[line[1]])
        else:
            error("RETURN takes 1 input, not " + str(len(line) - 1) + "\n" + "Line " + str(n + 1))
            exiting = True
    if line[0] == "VAR":
        if len(line) == 2:
            try:
                line[1] = int(line[1])
                error("Variable name cannot be a number" + "\n" + "Line " + str(n + 1))
                exiting = True
                
            except:
                storage[line[1]] = 0
        else:
            error("VAR takes 1 input, not " + str(len(line) - 1) + "\n" + "Line " + str(n + 1))
            exiting = True

    if line[0] == "ADD":
        if len(line) == 2:
            try:
                useless = storage[line[1]]
                storage[line[1]] += 1
            except:
                error("Variable " + str(line[2]) + " does not exist" + "\n" + "Line " + str(n + 1))
                exiting = True
        else:
            error("ADD takes 1 inputs, not " + str(len(line) - 1) + "\n" + "Line " + str(n + 1))
            exiting = True

    if line[0] == "SUB":
        if len(line) == 2:
            try:
                useless = storage[line[1]]
                storage[line[1]] -= 1
            except:
                    error("Variable " + str(line[1]) + " does not exist" + "\n" + "Line " + str(n + 1))
                    exiting = True
        else:
            error("SUB takes 1 input, not " + str(len(line) - 1) + "\n" + "Line " + str(n + 1))
            exiting = True

    if line[0] == "GOTO":
        if len(line) == 4:
            try:
                op1 = int(line[1])
            except:
                try:
                    op1 = storage[line[1]]
                except:
                    error("Variable " + str(line[1]) + " does not exist" + "\n" + "Line " + str(n + 1))
                    exiting = True
            try:
                op2 = int(line[2])
            except:
                try:
                    op2 = storage[line[2]]
                except:
                    error("Variable " + str(line[2]) + " does not exist" + "\n" + "Line " + str(n + 1))
                    exiting = True
            if not exiting and op1 == op2:
                try:
                    line[3] = int(line[3])
                    if line[3] - 1 >= 0 and line[3] - 1 <= len(lines):
                        n = line[3] - 2
                    else:
                        error("Third input must be a valid line number" + "\n" + "Line " + str(n + 1))
                        exiting = True
                except:
                    error("Third input must be a number" + "\n" + "Line " + str(n + 1))
                    exiting = True
        else:
            error("GOTO takes 3 inputs, not " + str(len(line) - 1) + "\n" + "Line " + str(n + 1))
            exiting = True
    else:
        error("Function " + line[0] + " does not exist" + "\n" + "Line " + str(n + 1))
        exiting = True 
            
    n += 1

#print(storage)
input()
