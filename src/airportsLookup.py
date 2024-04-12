# Create a lookup table (maybe a simple dict) for airports 
# a key could be IATA code and a value could be a name of airport

def airportLookup():
    path = "../data/airports.txt"
    mydict = {}

    with open(path, encoding="utf8") as filedata:
        for line in filedata.readlines():
            line = line.split(',')
            key = line[4].strip('"')
            value = line[1].strip('"')
            if key in mydict:
                mydict[key].append(value)
            else:
                mydict[key] = [value]
    return mydict

dict = airportLookup()
print(dict['SXX'])


