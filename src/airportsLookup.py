# Create a lookup table (maybe a simple dict) for airports 
# a key could be IATA code and a value could be a name of airport

# extract airports.txt and store aiports name and id in dict

# key = airport code, value = airport name
def airportLookup() -> dict:

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

# key = airport name, value = country name
def countryLookup() -> dict:

    path = "../data/airports.txt"
    mydict = {}

    with open(path, encoding="utf8") as filedata:
        for line in filedata.readlines():
            line = line.split(',')
            key = line[1].strip('"')
            value = line[3].strip('"')
            print(key, " : ", value)
            if key in mydict:
                mydict[key].append(value)
            else:
                mydict[key] = [value]

    return mydict


def generate_result(dict) -> list:

    file = "output.txt"
    list = [] 

    with open(file) as f:
        for line in f.readlines():
            line = line.split(',')
            code = line[0]
            list.append(code)
    
    return list


def main():
    codeToAirport = airportLookup()
    airportToCountry = countryLookup()
    generate_result(codeToAirport, airportToCountry)
    return 


if __name__ == "__main__":
    main()

