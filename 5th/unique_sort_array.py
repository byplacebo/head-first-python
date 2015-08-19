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
james = sorted([sanitize(each_t) for each_t in data.strip().split(",")])
with open("julie.txt") as jaf:
    data = jaf.readline()
julie = sorted([sanitize(each_t) for each_t in data.strip().split(",")])
with open("mikey.txt") as jaf:
    data = jaf.readline()
mikey = sorted([sanitize(each_t) for each_t in data.strip().split(",")])
with open("sarah.txt") as jaf:
    data = jaf.readline()
sarah = sorted([sanitize(each_t) for each_t in data.strip().split(",")])

clean_james = []
clean_julie = []
clean_mikey = []
clean_sarah = []

for each_t in james:
    if each_t not in clean_james:
        clean_james.append(sanitize(each_t))
for each_t in julie:
    if each_t not in clean_julie:
        clean_julie.append(sanitize(each_t))
for each_t in mikey:
    if each_t not in clean_mikey:
        clean_mikey.append(sanitize(each_t))
for each_t in sarah:
    if each_t not in clean_sarah:
        clean_sarah.append(sanitize(each_t))

print(clean_james[0:3])
print(clean_julie[0:3])
print(clean_mikey[0:3])
print(clean_sarah[0:3])

