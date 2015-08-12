import os;
print(os.getcwd())
#if os.path.exists("sketch.tx1t"):
try:
    data = open("sketch.txt")
    for each_line in data:
        #if not each_line.find(":") == -1:
        try:
            (role, line_spoken) = each_line.split(":", 1)
            print(role, end='')
            print(" said: ", end="")
            print(line_spoken, end="")
        except ValueError:
            pass
    data.close();
#else:
except IOError:
    print("The data file is missing!")

