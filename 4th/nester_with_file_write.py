import nester

man = []
other = []
try:
    with open("sketch.txt") as data:
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
    with open("man_file.txt", "w") as man_file, open("other_file.txt", "w") as other_file:
        nester.print_lol(man, fh=man_file)
        nester.print_lol(other, other_file)
except IOError as err:
        print("File Error : " + str(err))

