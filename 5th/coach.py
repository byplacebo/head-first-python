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

print(james)
print(julie)
print(mikey)
print(sarah)

