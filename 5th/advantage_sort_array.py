def sanitize(time_string):
    if "-" in time_string:
        splitter = "-"
    elif ":" in time_string:
        splitter = ":"
    else:
        return time_string
    (mins, secs) = time_string.split(splitter)
    return mins + "." + secs

with open("james.txt") as jaf:
    data = jaf.readline()
james = data.strip().split(",")

with open("julie.txt") as jaf:
    data = jaf.readline()
julie = data.strip().split(",")

with open("mikey.txt") as jaf:
    data = jaf.readline()
mikey = data.strip().split(",")

with open("sarah.txt") as jaf:
    data = jaf.readline()
sarah = data.strip().split(",")

print(sorted([sanitize(each_t) for each_t in james]))
print(sorted([sanitize(each_t) for each_t in julie]))
print(sorted([sanitize(each_t) for each_t in mikey]))
print(sorted([sanitize(each_t) for each_t in sarah]))

