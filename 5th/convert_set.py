def sanitize(time_string):
    if "-" in time_string:
        splitter = "-"
    elif ":" in time_string:
        splitter = ":"
    else:
        return time_string
    (mins, secs) = time_string.split(splitter)
    return mins + "." + secs


def get_coach_data(filename):
    try:
        with open(filename) as f:
            data = f.readline()
            return data.strip().split(",")
    except IOError as err:
        print("File error : " + str(err))
        return None


with open("james.txt") as jaf:
    data = jaf.readline()
james = data.strip().split(",")

with open("julie.txt") as jaf:
    data = jaf.readline()
julie = data.strip().split(",")

with open("mikey.txt") as jaf:
    data = jaf.readline()
mikey = data.strip().split(",")

print(sorted(set([sanitize(each_t) for each_t in james]))[0:3])
print(sorted(set([sanitize(each_t) for each_t in julie]))[0:3])
print(sorted(set([sanitize(each_t) for each_t in mikey]))[0:3])
print(sorted(set([sanitize(each_t) for each_t in get_coach_data("sarah.txt")]))[0:3])
