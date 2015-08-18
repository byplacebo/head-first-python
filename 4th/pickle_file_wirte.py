import pickle
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
    with open("man_file_b.txt", "wb") as man_file, open("other_file_b.txt", "wb") as other_file:
        pickle.dump(man, man_file)
        pickle.dump(other, other_file)
except IOError as err:
    print("File Error : " + str(err))

try:
    with open("man_file_b.txt", "rb") as man_read:
        new_man = pickle.load(man_read)
except IOError as err:
    print("File error: " + str(err))
except pickle.PickleError as perr:
    print("Pickling error: " + str(perr))

nester.print_lol(new_man)
print(new_man[0])
print(new_man[-1])
