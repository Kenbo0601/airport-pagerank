path = "../data/routes.txt"
file = open("source-dest.txt", 'w')
L = []
with open(path, encoding="utf8") as filedata:
    for line in filedata.readlines():
        line = line.split(',')
        source = line[2]
        dest = line[4]
        L.append(source + " - " + dest + "\n")
file.writelines(L)
file.close()

