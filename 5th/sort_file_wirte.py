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

clean_james = []
clean_julie = []
clean_mikey = []
clean_sarah = []

for each_t in james:
    clean_james.append(sanitize(each_t))
for each_t in julie:
    clean_julie.append(sanitize(each_t))
for each_t in mikey:
    clean_mikey.append(sanitize(each_t))
for each_t in sarah:
    clean_sarah.append(sanitize(each_t))

print(sorted(clean_james))
print(sorted(clean_julie))
print(sorted(clean_mikey))
print(sorted(clean_sarah))

