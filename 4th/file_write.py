man = []
other = []
try:
    #data = open("sketch.tx")
    data = open("sketch.txt")
    for each_line in data:
        try:
            (role, line_spoken) = each_line.split(':', 1)
            line_spoken = line_spoken.strip()
            if role == "Man":
                man.append(line_spoken)
            elif role == "Other Man":
                other.append(line_spoken)
        except ValueError:
            pass
    data.close()
except IOError as err:
    print("The datafile is missing! : " + str(err))

try:
    man_file = open("man_file.txt", "w")
    other_file = open("other_file.txt", "w")
    print(man, file=man_file)
    print(other, file=other_file)
except IOError as err:
    print("File Error : " + str(err))
finally:
    if "man_file" in locals():
        man_file.close()
    if "other_file" in locals():
        other_file.close()

